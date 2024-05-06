import java.util.Random;
import java.util.Scanner;

abstract class Guss{
    private int userInput;
    private int OurInput;
    abstract public int gussNumber();

    public int getUserInput() {
        return userInput;
    }
    public void setUserInput(int userInput) {
        this.userInput = userInput;
    }
    public int getOurInput() {
        return OurInput;
    }
    public void setOurInput(int ourInput) {
        OurInput = ourInput;
    }
    
}

class Processing extends Guss{
    @Override
    public int gussNumber() {
       if (super.getOurInput()==super.getUserInput()) {
        System.out.println("YOU GUSSED CORRECCT..");
        return 0;
       }
       else{      
        if (super.getUserInput() < super.getOurInput()) {
            System.out.println("Too low...Try again..");
            return -1;
        }
        else{
            System.out.println("Too high..Try again..");
            return -1;
        }
       }
    }
}

public class NumberGussingGame extends Processing{
    public static void main(String[] args) {
        Guss g = new Processing();
        Random random =new Random();
        Scanner scan = new Scanner(System.in);

        g.setOurInput(random.nextInt(10) + 1);
        System.out.println("Guss a number between 1 and 10");
        g.setUserInput(scan.nextInt());

        while(g.gussNumber() != 0)
        { 
            System.out.println("Guss a number between 1 and 10");
            g.setUserInput(scan.nextInt());
            
        }
        scan.close();

    }
}
