import java.io.IOException;

class Calculation {
    public static void main(String[] args) throws IOException {
        System.out.println("This is an addition calculator.");
        java.io.DataInput in = new java.io.DataInputStream(System.in);
        while (true) {
            System.out.println("Input your first number, press enter, then input your second number, press enter.");
            try {
                System.out.println(
                        "Your result is: " + (Double.parseDouble(in.readLine()) + Double.parseDouble(in.readLine())));
                break;
            } catch (NumberFormatException e) {
                System.out.println("Sorry but your input wasn't in the correct format");
            }
        }
    }
}