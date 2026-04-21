import javax.swing.*;
import java.awt.*;
import java.awt.image.*;
import java.io.*;
import javax.imageio.ImageIO;

public class Main {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Dressing Room");
            frame.setExtendedState(JFrame.MAXIMIZED_BOTH);
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

            try {
                BufferedImage background = ImageIO.read(new File("assets/backgrounds/DressingRoom.png"));

                JPanel panel = new JPanel() {
                    protected void paintComponent(Graphics g) {
                        super.paintComponent(g);
                        g.drawImage(background, 0, 0, getWidth(), getHeight(), this);
                    }
                };

                panel.setLayout(new BorderLayout());
                panel.add(new Character(), BorderLayout.CENTER);

                frame.setContentPane(panel);
                frame.setVisible(true);

            } catch (IOException e) {
                e.printStackTrace();
                JOptionPane.showMessageDialog(null, "Could not load background image.");
            }
        });
    }
}