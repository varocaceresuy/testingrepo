// This file es LF enforced in .gitattributes

// Module doc 😂 汉字.

/**
 * First comment line.
 * 
 * Extra doc
 * @returns some
 */
// should be ignored
function func1(param1) {
    // inline comment with multibyte chars 😂 汉字.
    return 1;
}

/**
 * anonymous function
 */
 const func2 = function() {
    // no doc 
    const func2_1 = function() {}
 }
 // no doc
 const func2_2 = function() {}
 
/**
 * arrow function
 */
 const func3 = () => {}

 var obj = {}

 /**
  * object property function 
  */
 obj.func4 = function() {}

/**
 * Class doc
 */
class ExampleClass {
    /**
     * Method doc
     */
    method1(param1) {
        return true;
    }
}

/**
 * anonymous class
 */
const class1 = class {
    method2() {};
}

/**
 * React example
 * @returns component
 */
function render() {
    return (<Comp attr={x}><h1>some text</h1></Comp>);
}
