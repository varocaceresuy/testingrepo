// This file es LF enforced in .gitattributes
/** 
 * Class doc 😂 汉字.
 */
public class ExampleClass {

    public static int exampleMethod(String param1) {
        // inline comment with multibyte chars 😂 汉字.
        return 1;
    }

    /**
     * <p>Method doc.</p>
     *
     * @param param2 text
     * value from param2 continues
     * @return {@link String} value
     */
    public void docstring(String param2) {
        return 1;
    }

    private class InnerClass{
        void innerMethod() {
            return;
        }
    }
    public ExampleClass() {
    }

    enum EnumExample {
        X;
        public int enumMethod() {
            return 1;
        }
    }

    public interface InterfaceExample {

        default int defaultMethod() {
            return 1;
        }

        float emptyFunction();
    }
}

