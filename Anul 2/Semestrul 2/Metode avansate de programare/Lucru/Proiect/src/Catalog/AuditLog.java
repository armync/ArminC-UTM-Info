package Catalog;

import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class AuditLog {

    private static final String FILENAME = "Audit.csv";

    public static void writeAuditLog(String action) {
        try (PrintWriter writer = new PrintWriter(new FileWriter(FILENAME, true))) {
            String timestamp = getCurrentTimestamp();
            writer.println(timestamp + "," + action);
        } catch (IOException e) {
            System.out.println("An error occurred while writing the audit log entry.");
            e.printStackTrace();
        }
    }

    private static String getCurrentTimestamp() {
        LocalDateTime currentDateTime = LocalDateTime.now();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        return currentDateTime.format(formatter);
    }
}
