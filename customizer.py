import pygame
import os
from typing import Optional

class Customizer:

    # base dimensions for scaling
    BASE_WIDTH = 1300
    BASE_HEIGHT = 1900
    SCALE_MULTIPLIER = 1.3

    # asset paths and options
    SKIN_NAMES       = ["Black.png", "Dark.png", "Brown.png", "Tan.png", "Olive.png", "Light.png", "White.png"]
    SKIN_PATH        = os.path.join("assets", "characters", "mc", "skins")
    SWIMWEAR_OUTFITS = ["Baywatch.png", "Leopard.png", "Blue.png", "Glitter.png", "Gold.png", "Bandeau.png"]
    EVERYDAY_OUTFITS = ["Milf.png", "Jorts.png", "Underboob.png", "Bows.png", "Cheetah.png", "EmoLace.png", "FairyLace.png", "PolkaDots.png", "Ruffles.png"]
    FORMAL_OUTFITS   = ["BugSuit.png", "LBD.png", "Silver.png", "Clown.png", "Ruffle.png"]
    SLEEPWEAR_OUTFITS = ["SoftSet.png", "EmoLace.png", "ButterflySet.png", "PolkaSlip.png", "SkimsSet.png", "Tee.png"]
    OUTFIT_PATHS     = [
        os.path.join("assets", "characters", "mc", "outfits", "swimsuits"),
        os.path.join("assets", "characters", "mc", "outfits", "everyday"),
        os.path.join("assets", "characters", "mc", "outfits", "formal"),
        os.path.join("assets", "characters", "mc", "outfits", "sleepwear")
    ]
    HAIR_COLORS      = ["Black", "Brown", "Red", "Ginger", "Honey", "Blonde", "Platinum"]
    HAIR_STYLES      = ["Straight.png", "Blowout.png", "HalfUp.png", "Braids.png", "Bob.png", "Buns.png"]
    HAIR_PATH        = os.path.join("assets", "characters", "mc", "hairs")
    NOSE_SHAPES      = ["Small.png", "Wide.png", "Angular.png"]
    NOSE_PATH        = os.path.join("assets", "characters", "mc", "face", "Nose")
    LIP_SHAPES       = ["Big", "Med", "Thin"]
    LIP_COLORS       = ["RumRaisin.png", "PillowTalk.png", "Bubblegum.png", "Berry.png", "Bean.png", "Black.png"]
    LIP_PATH         = os.path.join("assets", "characters", "mc", "face", "Mouth")
    EYE_SHAPES       = ["Sultry", "Doe", "Cat", "Sleepy"]
    EYE_COLORS       = ["Brown.png", "Green.png", "Blue.png"]
    EYE_PATH         = os.path.join("assets", "characters", "mc", "face", "Eyes")
    BROW_STYLES      = ["Thin.png", "Thick.png", "Cunt.png", "Bleached.png", "None"]
    BROW_PATH        = os.path.join("assets", "characters", "mc", "face", "Brows")
    TATTOOS          = ["None", "CollarboneIns.png", "HipIns.png", "HiPus.png", "xoxoBoob.png", "AnchorArm.png", "Xboob.png", "HeartHip.png", "SnakeArm.png"]
    TATTOO_PATH      = os.path.join("assets", "characters", "mc", "tattoos")

    def __init__(self):
        pygame.init()

        # instance variables
        self.running = True
        self.screen_info = pygame.display.Info()
        self.screenW, self.screenH = self.screen_info.current_w, self.screen_info.current_h
        self.screen = pygame.display.set_mode((self.screenW, self.screenH), pygame.RESIZABLE)
        pygame.display.set_caption("Customizer")
        self.clock = pygame.time.Clock()

        # window icon
        icon_path = os.path.join("assets", "UI", "logo.png")
        icon_surface = pygame.image.load(icon_path).convert_alpha()
        pygame.display.set_icon(icon_surface)

        # load background
        bg_path = os.path.join("assets", "backgrounds", "DressingRoom.png")
        self.background = pygame.image.load(bg_path).convert()

        # font & colours
        self.font = pygame.font.Font(None, 24)
        self.white, self.orange = (255,255,255), (240,182,144)

        # exit button
        self.exit_btn = pygame.Rect(self.screenW - 90, 10, 80, 30)

        # current indices
        self.skin_idx    = 0
        self.cat_idx     = 0  # 0 = swim, 1 = everyday, 2 = formal, 3 = sleepwear
        self.outfit_idx  = 0
        self.hair_color  = 0
        self.hair_style  = 0
        self.nose_idx    = 0
        self.lip_shape   = 0
        self.lip_color   = 0
        self.eye_shape   = 0
        self.eye_color   = 0
        self.brow_style  = 0
        self.tattoo_idx  = 0

        # load layer images
        self.labels: dict[str, Optional[pygame.Surface]] = {}  # name → pygame.Surface
        for name in ("skin","outfit","hair_back","hair_front","nose","lip","eye","brow","tattoo"):
            self.labels[name] = None

        # create UI buttons
        self.buttons = []
        self._init_buttons()

    def _init_buttons(self):
        # left panel: styles
        y = 80
        for text, cb in [
            ("Hair Style", lambda: self._cycle("hair_style",   self.HAIR_STYLES)),
            ("Nose Shape", lambda: self._cycle("nose_idx",     self.NOSE_SHAPES)),
            ("Lip Shape",  lambda: self._cycle("lip_shape",    self.LIP_SHAPES)),
            ("Eye Shape",  lambda: self._cycle("eye_shape",    self.EYE_SHAPES)),
            ("Brows",      lambda: self._cycle("brow_style",   self.BROW_STYLES)),
            ("Tattoos",    lambda: self._cycle("tattoo_idx",   self.TATTOOS))
        ]:
            rect = pygame.Rect(10, y, 180, 30);  y += 40
            self.buttons.append((rect, text, cb))

        # right panel: outfits & categories
        y = 80
        for text, cb in [
            ("Category",   lambda: self._cycle("cat_idx", [0,1,2,3])),
            ("Next Outfit",lambda: self._cycle("outfit_idx",
                [self.SWIMWEAR_OUTFITS, self.EVERYDAY_OUTFITS, self.FORMAL_OUTFITS, self.SLEEPWEAR_OUTFITS][self.cat_idx]))
        ]:
            rect = pygame.Rect(self.screenW - 190, y, 180, 30);  y += 40
            self.buttons.append((rect, text, cb))

        # color buttons
        y = 80 + 6*40
        for text, cb in [
            ("Skin Tone",    lambda: self._cycle("skin_idx",   self.SKIN_NAMES)),
            ("Hair Color",   lambda: self._cycle("hair_color", self.HAIR_COLORS)),
            ("Lipstick",     lambda: self._cycle("lip_color",  self.LIP_COLORS)),
            ("Eye Color",    lambda: self._cycle("eye_color",  self.EYE_COLORS))
        ]:
            rect = pygame.Rect(10, y, 180, 30);  y += 40
            self.buttons.append((rect, text, cb))

    def _cycle(self, attr, options):
        val = getattr(self, attr)
        val = (val + 1) % len(options)
        setattr(self, attr, val)
        if attr == "cat_idx":
            self.outfit_idx = 0
        self._reload_layers()

    def _reload_layers(self):
        # load each visual layer
        self.labels["skin"]   = pygame.image.load(os.path.join(self.SKIN_PATH, self.SKIN_NAMES[self.skin_idx])).convert_alpha()

        path = self.OUTFIT_PATHS[self.cat_idx]
        fname = [self.SWIMWEAR_OUTFITS, self.EVERYDAY_OUTFITS, self.FORMAL_OUTFITS, self.SLEEPWEAR_OUTFITS][self.cat_idx][self.outfit_idx]
        self.labels["outfit"] = pygame.image.load(os.path.join(path, fname)).convert_alpha()

        hairdir = self.HAIR_COLORS[self.hair_color]
        hairfile = self.HAIR_STYLES[self.hair_style]
        hair_base = hairfile.replace(".png", "")

        # Attempt to load hair_back and hair_front images
        back_path = os.path.join(self.HAIR_PATH, hairdir, f"{hair_base}_back.png")
        front_path = os.path.join(self.HAIR_PATH, hairdir, f"{hair_base}_front.png")
        single_path = os.path.join(self.HAIR_PATH, hairdir, f"{hairfile}")

        def load_image_optional(path):
            if os.path.exists(path):
                return pygame.image.load(path).convert_alpha()
            return None

        hair_back_img = load_image_optional(back_path)
        hair_front_img = load_image_optional(front_path)

        # If no split images exist, fallback to single hair image on front layer
        if not hair_back_img and not hair_front_img:
            hair_front_img = load_image_optional(single_path)
            hair_back_img = None

        self.labels["hair_back"] = hair_back_img
        self.labels["hair_front"] = hair_front_img

        skinfolder = self.SKIN_NAMES[self.skin_idx].replace(".png","")
        self.labels["nose"]   = pygame.image.load(os.path.join(self.NOSE_PATH, skinfolder, self.NOSE_SHAPES[self.nose_idx])).convert_alpha()

        ldir = self.LIP_SHAPES[self.lip_shape]
        lfile = self.LIP_COLORS[self.lip_color]
        self.labels["lip"]    = pygame.image.load(os.path.join(self.LIP_PATH, ldir, lfile)).convert_alpha()

        edir = self.EYE_SHAPES[self.eye_shape]
        efile = self.EYE_COLORS[self.eye_color]
        self.labels["eye"]    = pygame.image.load(os.path.join(self.EYE_PATH, edir, efile)).convert_alpha()

        bfile = self.BROW_STYLES[self.brow_style]
        self.labels["brow"] = None if bfile == "None" else pygame.image.load(os.path.join(self.BROW_PATH, bfile)).convert_alpha()

        tfile = self.TATTOOS[self.tattoo_idx]
        self.labels["tattoo"] = None if tfile == "None" else pygame.image.load(os.path.join(self.TATTOO_PATH, tfile)).convert_alpha()

    def _draw_background(self):
        bg = pygame.transform.scale(self.background, (self.screenW, self.screenH))
        self.screen.blit(bg, (0,0))

    def _draw_ui(self):
        pygame.draw.rect(self.screen, self.orange, self.exit_btn)
        ex = self.font.render("Exit", True, self.white)
        self.screen.blit(ex, ex.get_rect(center=self.exit_btn.center))

        for rect, text, _ in self.buttons:
            pygame.draw.rect(self.screen, self.orange, rect)
            surf = self.font.render(text, True, self.white)
            self.screen.blit(surf, surf.get_rect(center=rect.center))
        
        # draw category label
        categories = ["Swimwear", "Everyday", "Formal", "Sleepwear"]
        label_text = f"Category: {categories[self.cat_idx]}"
        label_surface = self.font.render(label_text, True, (0, 100, 0))  # dark green text
        label_rect = label_surface.get_rect()
        label_rect.topleft = (10, self.screenH - 40)
        bg_rect = pygame.Rect(label_rect.left - 5, label_rect.top - 2, label_rect.width + 10, label_rect.height + 4)
        pygame.draw.rect(self.screen, self.orange, bg_rect)
        self.screen.blit(label_surface, label_rect)

    def _draw_character(self):
        # center character & scale
        scale = min(self.screenW/self.BASE_WIDTH, self.screenH/self.BASE_HEIGHT) * self.SCALE_MULTIPLIER
        w, h = int(self.BASE_WIDTH*scale), int(self.BASE_HEIGHT*scale)
        x = (self.screenW - w)//2
        y = (self.screenH - h)//15

        # draw body parts and clothes
        for layer in ["skin","tattoo","nose","lip","eye","brow"]:
            img = self.labels[layer]
            if img:
                img_scaled = pygame.transform.smoothscale(img, (w,h))
                self.screen.blit(img_scaled, (x,y))
                
        # draw back hair first (if it exists)
        if self.labels["hair_back"]:
            img_scaled = pygame.transform.smoothscale(self.labels["hair_back"], (w,h))
            self.screen.blit(img_scaled, (x,y))
            
         # draw outfit (on top of back hair)
        if self.labels["outfit"]:
            img_scaled = pygame.transform.smoothscale(self.labels["outfit"], (w,h))
            self.screen.blit(img_scaled, (x,y))


        # draw front hair last (if it exists)
        if self.labels["hair_front"]:
            img_scaled = pygame.transform.smoothscale(self.labels["hair_front"], (w,h))
            self.screen.blit(img_scaled, (x,y))

    def _handle_event(self, evt):
        if evt.type == pygame.QUIT:
            self.running = False
        elif evt.type == pygame.VIDEORESIZE:
            self.screenW, self.screenH = evt.w, evt.h
            self.screen = pygame.display.set_mode((self.screenW, self.screenH), pygame.RESIZABLE)
            self.exit_btn.topleft = (self.screenW-90,10)
        elif evt.type == pygame.MOUSEBUTTONDOWN:
            if self.exit_btn.collidepoint(evt.pos):
                self.running = False
            for rect, _, cb in self.buttons:
                if rect.collidepoint(evt.pos):
                    cb()

    def overall(self):
        self._reload_layers()
        while self.running:
            for evt in pygame.event.get():
                self._handle_event(evt)
            self._draw_background()
            self._draw_character()
            self._draw_ui()
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()

    def get_character(self):
        return {
            "skin":    self.SKIN_NAMES[self.skin_idx],
            "category": self.cat_idx,
            "outfit":  self.outfit_idx,
            "hair":    (self.HAIR_COLORS[self.hair_color], self.HAIR_STYLES[self.hair_style]),
            "nose":    self.NOSE_SHAPES[self.nose_idx],
            "lip":     (self.LIP_SHAPES[self.lip_shape], self.LIP_COLORS[self.lip_color]),
            "eye":     (self.EYE_SHAPES[self.eye_shape], self.EYE_COLORS[self.eye_color]),
            "brow":    self.BROW_STYLES[self.brow_style],
            "tattoo":  self.TATTOOS[self.tattoo_idx]
        }
