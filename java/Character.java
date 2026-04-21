import javax.swing.*;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;

public class Character extends JPanel {
    private static final String[] SKIN_NAMES = {"Black.png", "Brown.png", "Tan.png", "White.png"};
    private static final String SKIN_PATH = "assets/characters/mc/skins/";

    private static final String[] SWIMWEAR_OUTFITS = {"Baywatch.png", "Leopard.png", "Blue.png", "Glitter.png", "Gold.png", "Bandeau.png"};
    private static final String[] EVERYDAY_OUTFITS = {"Milf.png", "Jorts.png", "Underboob.png"};
    private static final String SWIMWEAR_PATH = "assets/characters/mc/outfits/swimsuits/";
    private static final String EVERYDAY_PATH = "assets/characters/mc/outfits/everyday/";

    private static final String[] HAIR_COLORS = {"Black", "Brown", "Red", "Honey", "Platinum"};
    private static final String[] HAIR_STYLES = {"Straight.png", "Blowout.png", "HalfUp.png", "Braids.png", "Bob.png", "Buns.png"};
    private static final String HAIR_PATH = "assets/characters/mc/hairs/";

    private static final String[] NOSE_SHAPES = {"Small.png", "Wide.png", "Angular.png"};
    private static final String NOSE_PATH = "assets/characters/mc/face/Nose/";

    private static final String[] LIP_SHAPES = {"Big", "Med", "Thin"};
    private static final String[] LIP_COLORS = {"RumRaisin.png", "PillowTalk.png", "Bubblegum.png", "Berry.png"};
    private static final String LIP_PATH = "assets/characters/mc/face/Mouth/";

    private static final String[] EYE_SHAPES = {"Sultry", "Doe", "Cat"};
    private static final String[] EYE_COLORS = {"Brown.png", "Green.png", "Blue.png"};
    private static final String EYE_PATH = "assets/characters/mc/face/Eyes/";

    // === Eyebrows ===
    private static final String[] BROW_STYLES = {"Thin.png", "Thick.png", "Cunt.png", "None"};
    private static final String BROW_PATH = "assets/characters/mc/face/Brows/";

    private int currentSkinIndex = 0;
    private int currentCategoryIndex = 0;
    private int currentOutfitIndex = 0;
    private int currentHairColorIndex = 0;
    private int currentHairStyleIndex = 0;
    private int currentNoseShapeIndex = 0;
    private int currentLipShapeIndex = 0;
    private int currentLipColorIndex = 0;
    private int currentEyeShapeIndex = 0;
    private int currentEyeColorIndex = 0;
    private int currentBrowStyleIndex = 0;

    private JLabel skinLabel;
    private JLabel outfitLabel;
    private JLabel hairLabel;
    private JLabel noseLabel;
    private JLabel lipLabel;
    private JLabel eyeLabel;
    private JLabel browLabel;

    public Character() {
        setOpaque(false);
        setLayout(new BorderLayout());

        // === Left Panel ===
        JPanel leftPanel = new JPanel();
        leftPanel.setLayout(new BoxLayout(leftPanel, BoxLayout.Y_AXIS));
        leftPanel.setOpaque(false);

        leftPanel.add(wrap(createButton("Hair Style", () -> {
            currentHairStyleIndex = (currentHairStyleIndex + 1) % HAIR_STYLES.length;
            updateHairImage();
        })));

        leftPanel.add(wrap(createButton("Nose Shape", () -> {
            currentNoseShapeIndex = (currentNoseShapeIndex + 1) % NOSE_SHAPES.length;
            updateNoseImage();
        })));

        leftPanel.add(wrap(createButton("Lip Shape", () -> {
            currentLipShapeIndex = (currentLipShapeIndex + 1) % LIP_SHAPES.length;
            updateLipImage();
        })));

        leftPanel.add(wrap(createButton("Eye Shape", () -> {
            currentEyeShapeIndex = (currentEyeShapeIndex + 1) % EYE_SHAPES.length;
            updateEyeImage();
        })));

        // === Brow Style Button ===
        leftPanel.add(wrap(createButton("Brows", () -> {
            currentBrowStyleIndex = (currentBrowStyleIndex + 1) % BROW_STYLES.length;
            updateBrowImage();
        })));

        // === Color Panel ===
        JPanel colorPanel = new JPanel();
        colorPanel.setLayout(new BoxLayout(colorPanel, BoxLayout.Y_AXIS));
        colorPanel.setOpaque(false);

        colorPanel.add(wrap(createButton("Skin Tone", () -> {
            currentSkinIndex = (currentSkinIndex + 1) % SKIN_NAMES.length;
            updateSkinImage();
            updateNoseImage();
        })));

        colorPanel.add(wrap(createButton("Hair Color", () -> {
            currentHairColorIndex = (currentHairColorIndex + 1) % HAIR_COLORS.length;
            updateHairImage();
        })));

        colorPanel.add(wrap(createButton("Lipstick", () -> {
            currentLipColorIndex = (currentLipColorIndex + 1) % LIP_COLORS.length;
            updateLipImage();
        })));

        colorPanel.add(wrap(createButton("Eye Color", () -> {
            currentEyeColorIndex = (currentEyeColorIndex + 1) % EYE_COLORS.length;
            updateEyeImage();
        })));

        JPanel containerPanel = new JPanel(new BorderLayout());
        containerPanel.setOpaque(false);
        containerPanel.add(leftPanel, BorderLayout.WEST);
        containerPanel.add(colorPanel, BorderLayout.CENTER);
        add(containerPanel, BorderLayout.WEST);

        // === Right Panel ===
        JPanel rightPanel = new JPanel();
        rightPanel.setLayout(new BoxLayout(rightPanel, BoxLayout.Y_AXIS));
        rightPanel.setOpaque(false);

        rightPanel.add(wrap(createButton("Category", () -> {
            currentCategoryIndex = (currentCategoryIndex + 1) % 2;
            currentOutfitIndex = 0;
            updateOutfitImage();
        })));

        rightPanel.add(wrap(createButton("Next Outfit", () -> {
            if (currentCategoryIndex == 0) {
                currentOutfitIndex = (currentOutfitIndex + 1) % SWIMWEAR_OUTFITS.length;
            } else {
                currentOutfitIndex = (currentOutfitIndex + 1) % EVERYDAY_OUTFITS.length;
            }
            updateOutfitImage();
        })));

        add(rightPanel, BorderLayout.EAST);

        // === Labels ===
        skinLabel = new JLabel();
        outfitLabel = new JLabel();
        hairLabel = new JLabel();
        noseLabel = new JLabel();
        lipLabel = new JLabel();
        eyeLabel = new JLabel();
        browLabel = new JLabel();

        for (JLabel label : new JLabel[]{skinLabel, outfitLabel, hairLabel, noseLabel, lipLabel, eyeLabel, browLabel}) {
            label.setAlignmentY(0.8f);
            label.setBorder(BorderFactory.createEmptyBorder(100, 0, 0, 0));
        }

        JPanel layeredPanel = new JPanel();
        layeredPanel.setLayout(new OverlayLayout(layeredPanel));
        layeredPanel.setOpaque(false);
        layeredPanel.setPreferredSize(new Dimension(1300, 1900));

        layeredPanel.add(hairLabel);
        layeredPanel.add(browLabel); // Added here
        layeredPanel.add(noseLabel);
        layeredPanel.add(lipLabel);
        layeredPanel.add(eyeLabel);
        layeredPanel.add(outfitLabel);
        layeredPanel.add(skinLabel);

        JPanel centerPanel = new JPanel(new GridBagLayout());
        centerPanel.setOpaque(false);
        centerPanel.add(layeredPanel);
        add(centerPanel, BorderLayout.CENTER);

        // === Initial updates ===
        updateSkinImage();
        updateOutfitImage();
        updateHairImage();
        updateNoseImage();
        updateLipImage();
        updateEyeImage();
        updateBrowImage();
    }

    private JButton createButton(String text, Runnable action) {
        JButton button = new JButton(text);
        button.setFont(new Font("Georgia", Font.BOLD, 28));
        button.setPreferredSize(new Dimension(200, 60));
        button.setBackground(new Color(27, 60, 52, 153));
        button.setForeground(Color.WHITE);
        button.setOpaque(true);
        button.setBorderPainted(false);
        button.addActionListener(e -> action.run());
        return button;
    }

    private JPanel wrap(JComponent comp) {
        JPanel wrapper = new JPanel(new FlowLayout(FlowLayout.LEFT));
        wrapper.setOpaque(false);
        wrapper.setBorder(BorderFactory.createEmptyBorder(20, 30, 0, 0));
        wrapper.add(comp);
        return wrapper;
    }

    private void updateSkinImage() {
        try {
            BufferedImage skin = ImageIO.read(new File(SKIN_PATH + SKIN_NAMES[currentSkinIndex]));
            Image scaled = skin.getScaledInstance(1300, 1900, Image.SCALE_SMOOTH);
            skinLabel.setIcon(new ImageIcon(scaled));
        } catch (IOException e) {
            e.printStackTrace();
            skinLabel.setIcon(null);
        }
    }

    private void updateOutfitImage() {
        String file = (currentCategoryIndex == 0) ? SWIMWEAR_OUTFITS[currentOutfitIndex] : EVERYDAY_OUTFITS[currentOutfitIndex];
        String path = (currentCategoryIndex == 0) ? SWIMWEAR_PATH : EVERYDAY_PATH;
        try {
            BufferedImage outfit = ImageIO.read(new File(path + file));
            Image scaled = outfit.getScaledInstance(1300, 1900, Image.SCALE_SMOOTH);
            outfitLabel.setIcon(new ImageIcon(scaled));
        } catch (IOException e) {
            e.printStackTrace();
            outfitLabel.setIcon(null);
        }
    }

    private void updateHairImage() {
        String path = HAIR_PATH + HAIR_COLORS[currentHairColorIndex] + "/" + HAIR_STYLES[currentHairStyleIndex];
        try {
            BufferedImage hair = ImageIO.read(new File(path));
            Image scaled = hair.getScaledInstance(1300, 1900, Image.SCALE_SMOOTH);
            hairLabel.setIcon(new ImageIcon(scaled));
        } catch (IOException e) {
            e.printStackTrace();
            hairLabel.setIcon(null);
        }
    }

    private void updateNoseImage() {
        String skinFolder = SKIN_NAMES[currentSkinIndex].replace(".png", "");
        String nosePath = NOSE_PATH + skinFolder + "/" + NOSE_SHAPES[currentNoseShapeIndex];
        try {
            BufferedImage nose = ImageIO.read(new File(nosePath));
            Image scaled = nose.getScaledInstance(1300, 1900, Image.SCALE_SMOOTH);
            noseLabel.setIcon(new ImageIcon(scaled));
        } catch (IOException e) {
            e.printStackTrace();
            noseLabel.setIcon(null);
        }
    }

    private void updateLipImage() {
        String file = LIP_SHAPES[currentLipShapeIndex] + "/" + LIP_COLORS[currentLipColorIndex];
        try {
            BufferedImage lips = ImageIO.read(new File(LIP_PATH + file));
            Image scaled = lips.getScaledInstance(1300, 1900, Image.SCALE_SMOOTH);
            lipLabel.setIcon(new ImageIcon(scaled));
        } catch (IOException e) {
            e.printStackTrace();
            lipLabel.setIcon(null);
        }
    }

    private void updateEyeImage() {
        String file = EYE_SHAPES[currentEyeShapeIndex] + "/" + EYE_COLORS[currentEyeColorIndex];
        try {
            BufferedImage eye = ImageIO.read(new File(EYE_PATH + file));
            Image scaled = eye.getScaledInstance(1300, 1900, Image.SCALE_SMOOTH);
            eyeLabel.setIcon(new ImageIcon(scaled));
        } catch (IOException e) {
            e.printStackTrace();
            eyeLabel.setIcon(null);
        }
    }

    private void updateBrowImage() {
        String browFile = BROW_STYLES[currentBrowStyleIndex];
        if (browFile.equals("None")) {
            browLabel.setIcon(null);
            return;
        }

        try {
            BufferedImage brows = ImageIO.read(new File(BROW_PATH + browFile));
            Image scaled = brows.getScaledInstance(1300, 1900, Image.SCALE_SMOOTH);
            browLabel.setIcon(new ImageIcon(scaled));
        } catch (IOException e) {
            e.printStackTrace();
            browLabel.setIcon(null);
        }
    }
}
