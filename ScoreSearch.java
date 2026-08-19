import java.util.Scanner;

public class ScoreSearch {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

       
        int[] scores = new int[5];

        for (int i = 0; i < scores.length; i++) {
            System.out.print("Enter Score " + (i + 1) + ": ");
            scores[i] = input.nextInt();
        }

        
        System.out.println("\nScores Entered:");
        for (int i = 0; i < scores.length; i++) {
            System.out.print(scores[i] + " ");
        }

        
        System.out.print("\n\nEnter score to search: ");
        int searchScore = input.nextInt();

        
        boolean found = false;
        int position = -1;
        int comparisons = 0;

       
        for (int i = 0; i < scores.length; i++) {

            comparisons++;

            if (scores[i] == searchScore) {
                found = true;
                position = i + 1;
                break;
            }
        }

        
        if (found) {
            System.out.println("\nScore Found!");
            System.out.println(searchScore + " is located at position " + position + ".");
        } else {
            System.out.println("\nScore Not Found.");
        }

        System.out.println("Number of Comparisons: " + comparisons);

        input.close();
    }
}