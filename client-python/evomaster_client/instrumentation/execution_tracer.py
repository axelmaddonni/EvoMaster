from typing import Sequence, Set

from evomaster_client.instrumentation import objective_naming


class AdditionalInfo:
    def __init__(self) -> None:
        self.query_parameters = set()
        self.headers = set()
        self.last_executed_statement_stack = []
        self.no_exception_statement = None

    def push_last_executed_statement(self, last_line: str) -> None:
        self.no_exception_statement = None
        self.last_executed_statement_stack.append(last_line)

    def pop_last_executed_statement(self) -> str:
        statement = self.last_executed_statement_stack.pop()
        if not self.last_executed_statement_stack:
            self.no_exception_statement = statement
        return statement


class Action:
    def __init__(self, index: int, input_variables: Sequence[str]) -> None:
        self.index = index
        self.input_variables = input_variables


class TargetInfo:
    def __init__(self, mapped_id: int, descriptive_id: str, value: float, action_index: int):
        self.mapped_id = mapped_id
        self.descriptive_id = descriptive_id
        self.value = value
        self.action_index = action_index


class Singleton(object):
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            s = super(Singleton, cls).__new__(cls, *args, **kwargs)
            s.initialize()
            cls._instances[cls] = s
        return cls._instances[cls]

    def initialize(self):
        pass


class ExecutionTracer(Singleton):
    def initialize(self):
        self.reset()

    def reset(self) -> None:
        self.objective_coverage = {}
        self.action_index = 0
        self.input_variables = set()
        self.additional_info_list = []
        self.additional_info_list.append(AdditionalInfo())

    def set_action(self, action: Action) -> None:
        if action.index != self.action_index:
            self.action_index = action.index
            self.additional_info_list.append(AdditionalInfo())
        if action.input_variables:
            self.input_variables = action.input_variables

    def mark_last_executed_statement(self, last_line: str) -> None:
        self.additional_info_list[self.action_index].push_last_executed_statement(last_line)

    def completed_last_executed_statement(self, last_line: str) -> None:
        self.additional_info_list[self.action_index].pop_last_executed_statement()

    def get_number_of_objectives(self, prefix: str = '') -> int:
        return len([k for k in self.objective_coverage.keys() if k.startsWith(prefix)])

    def get_number_of_non_covered_objectives(self, prefix: str = '') -> int:
        return len(self.get_non_covered_objectives(prefix))

    def get_non_covered_objectives(self, prefix: str = '') -> Set[str]:
        return set(descriptive_id for descriptive_id, target_info in self.objective_coverage.items()
                   if descriptive_id.startsWith(prefix) and target_info.value < 1)

    def get_value(self, descriptive_id: str) -> float:
        return self.objective_coverage[descriptive_id].value

    def update_objective(self, descriptive_id: str, value: float) -> None:
        if value < 0 or value > 1:
            raise ValueError(f'Invalid value: {value}')
        target_info = TargetInfo(None, descriptive_id, value, self.action_index)
        previous = self.objective_coverage.get(descriptive_id)
        if previous:
            if value > previous.value:
                self.objective_coverage[descriptive_id] = target_info
        else:
            self.objective_coverage[descriptive_id] = target_info
        # TODO: ObjectiveRecorder.update(id, value)

    def entering_statement(self, file_name: str, line: int, statement: int) -> None:
        file_id = objective_naming.file_objective_name(file_name)
        line_id = objective_naming.line_objective_name(file_name, line)
        statement_id = objective_naming.statement_objective_name(file_name, line, statement)
        self.update_objective(file_id, 1)
        self.update_objective(line_id, 1)
        self.update_objective(statement_id, 0.5)
        self.mark_last_executed_statement(f"{file_name}_{line}_{statement}")

    def completed_statement(self, file_name: str, line: int, statement: int) -> None:
        statement_id = objective_naming.statement_objective_name(file_name, line, statement)
        self.update_objective(statement_id, 1)
        self.completed_last_executed_statement(f"{file_name}_{line}_{statement}")
        # HeuristicsForBooleans.clearLastEvaluation()

    # TODO: def update_branch(self, ...)