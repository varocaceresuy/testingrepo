class ExampleClass implements Logger {
  log(message: string, ...args: any[]) {
    output.print(`[${month}-${date} ${h}:${m}:${s}]`, message, ...args);
  }
  trace(message: string, ...args: any[]) {
    if (debug) {
      this.log('[trace]', message, ...args);
    }
  }
  /** arrow function */
  display = () => console.log('display')
}

/**
 * Docstring
 * @returns The parameters to be sent on each request.
 */
function getCommonParameters(): any {
    // inline comment with multibyte chars 😂 汉字.
    return {};
}

/** docstring 😂 morè téxt 汉字* */
async function weirdChar(requestParams: any,) {
    axiosReqConfig.params = {...requestParams, ...getCommonParameters()};
    const response = await axios.post(ANAYLTICSHOSTURL, null, axiosReqConfig);
    writeToAnalyticsLog(JSON.stringify(axiosReqConfig.params ));
}

// inner class
class Foo {
}

module Foo {
    export class InnerFoo {
      hello(){
        console.log('hello')
      }
    }
}

/** anonymous function */
var result = function(a:number, b:number) {
    return a+b
}

var c = result(12,2)

/**
 * React example
 * @returns component
 */
function render() {
    return (<Comp attr={x}><h1>some text</h1></Comp>);
}