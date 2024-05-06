import java.util.Random;
import java.util.Scanner;

public class RockPaperScissors {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        String[] choices = {"rock", "paper", "scissors"};

        while (true) {
            System.out.print("Enter your choice (rock, paper, or scissors): ");
            String playerChoice = scanner.nextLine().toLowerCase();

            if (!isValidChoice(playerChoice)) {
                System.out.println("Invalid choice. Please choose rock, paper, or scissors.");
                continue;
            }

            int computerIndex = random.nextInt(3);
            String computerChoice = choices[computerIndex];

            System.out.println("Computer chooses: " + computerChoice);
            System.out.println("You chose: " + playerChoice);

            String result = determineWinner(playerChoice, computerChoice);
            System.out.println(result);

            System.out.print("Play again? (yes/no): ");
            String playAgain = scanner.nextLine().toLowerCase();
            if (!playAgain.equals("yes")) {
                break;
            }
        }

        System.out.println("Thanks for playing!");
        scanner.close();
    }

    public static boolean isValidChoice(String choice) {
        return choice.equals("rock") || choice.equals("paper") || choice.equals("scissors");
    }

    public static String determineWinner(String player, String computer) {
        if (player.equals(computer)) {
            return "It's a tie!";
        } else if ((player.equals("rock") && computer.equals("scissors")) ||
                   (player.equals("paper") && computer.equals("rock")) ||
                   (player.equals("scissors") && computer.equals("paper"))) {
            return "You win!";
        } else {
            return "Computer wins!";
        }
    }
}
