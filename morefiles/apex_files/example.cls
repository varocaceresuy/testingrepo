/**
 * @description Class doc 😂 汉字`
 *
 * @group a tag
 */
global class ExampleClass {
    public String hello(String param1) {
        // inline comment with multibyte chars 😂 汉字.
        return 'Hello World!';
    }

    /**
     * Class doc 😂 汉字
     * @description description
     * @example
     * ExampleClass.hello()
     **/
    public void docstring(String param2) {
        return 1;
    }
    trigger myAccountTrigger on Account(before insert, before update) {
        if (Trigger.isBefore) {
            for (Account a : Trigger.old) {
                if (a.name != 'okToDelete') {
                    a.addError('You cannot delete this record!');
                }
            }
        }
    }

    static testmethod testFoo() {
        return 'Test';
    }
}

public interface ISObjects extends IObjects{

	List<SObject> emptyFunction();

    float normalFunction() {return 3.1;}
