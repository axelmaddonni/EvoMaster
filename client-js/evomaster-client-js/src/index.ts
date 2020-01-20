import plugin, {Babel, PluginOptions} from "./instrumentation/babel-plugin-evomaster";

import * as ControllerConstants from "./controller/api/ControllerConstants";
import EMController from "./controller/EMController";
import SutController from "./controller/SutController";

import AuthenticationDto from "./controller/api/dto/AuthenticationDto";
import ProblemInfo from "./controller/api/dto/problem/ProblemInfo";
import RestProblemDto from "./controller/api/dto/problem/RestProblemDto";
import {OutputFormat} from "./controller/api/dto/SutInfoDto";
import SutRunDto from "./controller/api/dto/SutRunDto";

import InjectedFunctions from "./instrumentation/InjectedFunctions";
import ExecutionTracer from "./instrumentation/staticstate/ExecutionTracer";
import ObjectiveRecorder from "./instrumentation/staticstate/ObjectiveRecorder";
import {Visitor} from "@babel/traverse";



interface EM {
    (babel: Babel):  {visitor: Visitor<PluginOptions>},
    SutController: typeof SutController,
    EMController: typeof EMController;
    // ControllerConstants: Array<string>; //FIXME
    dto: {
        AuthenticationDto: typeof AuthenticationDto,
        ProblemInfo: typeof ProblemInfo,
        RestProblemDto: typeof RestProblemDto,
        OutputFormat: typeof OutputFormat,
        SutRunDto: typeof SutRunDto
    },
    InjectedFunctions: typeof InjectedFunctions,
    internal: {
        ExecutionTracer: typeof ExecutionTracer,
        ObjectiveRecorder: typeof ObjectiveRecorder
    }
}

//@ts-ignore
const f : EM = plugin;
f.SutController =  SutController;
f.EMController = EMController;
f.dto = {
    AuthenticationDto: AuthenticationDto,
    ProblemInfo: ProblemInfo,
    RestProblemDto: RestProblemDto,
    OutputFormat: OutputFormat,
    SutRunDto: SutRunDto
};
f.InjectedFunctions = InjectedFunctions;
f.internal = {
    ExecutionTracer: ExecutionTracer,
    ObjectiveRecorder: ObjectiveRecorder
};

export = f;


// module.exports = plugin;
// const ex = module.exports;
//
// ex.SutController = SutController;
// ex.EMController = EMController;
// ex.ControllerConstants = ControllerConstants;
//
// ex.dto = {};
// ex.dto.AuthenticationDto = AuthenticationDto;
// ex.dto.ProblemInfo = ProblemInfo;
// ex.dto.RestProblemDto = RestProblemDto;
// ex.dto.OutputFormat = OutputFormat;
// ex.dto.SutRunDto = SutRunDto;
//
// //used by the instrumented SUT
// ex.InjectedFunctions = InjectedFunctions;
//
// //only needed for testing the instrumentation
// ex.internal.ExecutionTracer = ExecutionTracer;
// ex.internal.ObjectiveRecorder = ObjectiveRecorder;

