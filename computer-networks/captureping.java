import java.util.*;

public class captureping{
    public void Ping(String host){
        try{
            Process p = Runtime.getRuntime().exec("ping " + host);
            Scanner sc = new Scanner(p.getInputStream());

            while(sc.hasNextLine()){
                System.out.println(sc.nextLine());
            }
        }catch(Exception e){
            System.out.println(e);
        }
    }

    public static void main(String[] args){
        captureping p = new captureping();
        p.Ping("www.google.com");
    }
}

