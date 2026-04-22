// ── ASSET DEFINITIONS ──

const SKINS         = ["Black.png", "Dark.png", "Brown.png", "Tan.png", "Olive.png", "Light.png", "White.png"];
const SKIN_PATH     = "images/characters/mc/skins/";

const HAIR_COLORS   = ["Black", "Brown", "Red", "Ginger", "Honey", "Blonde", "Platinum"];
const HAIR_STYLES   = ["Straight", "Blowout", "HalfUp", "Braids", "Bob", "Buns"];
const SPLIT_HAIRS   = ["Straight", "HalfUp", "Braids"]; // have _back and _front
const HAIR_PATH     = "images/characters/mc/hairs/";

const NOSE_SHAPES   = ["Small.png", "Wide.png", "Angular.png"];
const NOSE_PATH     = "images/characters/mc/face/Nose/";

const LIP_SHAPES    = ["Big", "Med", "Thin"];
const LIP_COLORS    = ["RumRaisin.png", "PillowTalk.png", "Bubblegum.png", "Berry.png", "Bean.png", "Black.png"];
const LIP_PATH      = "images/characters/mc/face/Mouth/";

const EYE_SHAPES    = ["Sultry", "Doe", "Cat", "Sleepy"];
const EYE_COLORS    = ["Brown.png", "Green.png", "Blue.png"];
const EYE_PATH      = "images/characters/mc/face/Eyes/";

const BROW_STYLES   = ["Thin.png", "Thick.png", "Cunt.png", "Bleached.png", "None"];
const BROW_PATH     = "images/characters/mc/face/Brows/";

const TATTOOS       = ["None", "CollarboneIns.png", "HipIns.png", "HiPus.png", "xoxoBoob.png", "AnchorArm.png", "Xboob.png", "HeartHip.png", "SnakeArm.png"];
const TATTOO_PATH   = "images/characters/mc/tattoos/";

const CATEGORIES    = ["Swimwear", "Everyday", "Formal", "Sleepwear"];
const OUTFITS       = [
  ["Baywatch.png", "Leopard.png", "Blue.png", "Glitter.png", "Gold.png", "Bandeau.png"],           // swimsuits
  ["Milf.png", "Jorts.png", "Underboob.png", "Bows.png", "Cheetah.png", "EmoLace.png", "FairyLace.png", "PolkaDots.png", "Ruffles.png"], // everyday
  ["BugSuit.png", "LBD.png", "Silver.png", "Clown.png", "Ruffle.png"],                             // formal
  ["SoftSet.png", "EmoLace.png", "ButterflySet.png", "PolkaSlip.png", "SkimsSet.png", "Tee.png"]   // sleepwear
];
const OUTFIT_PATHS  = [
  "images/characters/mc/outfits/swimsuits/",
  "images/characters/mc/outfits/everyday/",
  "images/characters/mc/outfits/formal/",
  "images/characters/mc/outfits/sleepwear/"
];

// ── STATE ──

const state = {
  skin_idx:   0,
  cat_idx:    0,
  outfit_idx: 0,
  hair_color: 0,
  hair_style: 0,
  nose_idx:   0,
  lip_shape:  0,
  lip_color:  0,
  eye_shape:  0,
  eye_color:  0,
  brow_style: 0,
  tattoo_idx: 0
};

// ── LAYER ELEMENTS ──

const layers = {
  skin:      document.getElementById("layer-skin"),
  tattoo:    document.getElementById("layer-tattoo"),
  nose:      document.getElementById("layer-nose"),
  lip:       document.getElementById("layer-lip"),
  eye:       document.getElementById("layer-eye"),
  brow:      document.getElementById("layer-brow"),
  hairBack:  document.getElementById("layer-hair-back"),
  outfit:    document.getElementById("layer-outfit"),
  hairFront: document.getElementById("layer-hair-front")
};

// ── SCREENS ──

const mainMenu   = document.getElementById("main-menu");
const customizer = document.getElementById("customizer");

// ── RELOAD LAYERS ──

function reloadLayers() {

  // skin
  layers.skin.src = SKIN_PATH + SKINS[state.skin_idx];

  // tattoo
  if (TATTOOS[state.tattoo_idx] === "None") {
    layers.tattoo.src = "";
  } else {
    layers.tattoo.src = TATTOO_PATH + TATTOOS[state.tattoo_idx];
  }

  // nose (skin-matched folder)
  const skinFolder = SKINS[state.skin_idx].replace(".png", "");
  layers.nose.src = NOSE_PATH + skinFolder + "/" + NOSE_SHAPES[state.nose_idx];

  // lip
  layers.lip.src = LIP_PATH + LIP_SHAPES[state.lip_shape] + "/" + LIP_COLORS[state.lip_color];

  // eye
  layers.eye.src = EYE_PATH + EYE_SHAPES[state.eye_shape] + "/" + EYE_COLORS[state.eye_color];

  // brow
  if (BROW_STYLES[state.brow_style] === "None") {
    layers.brow.src = "";
  } else {
    layers.brow.src = BROW_PATH + BROW_STYLES[state.brow_style];
  }

  // hair
  const hairColor = HAIR_COLORS[state.hair_color];
  const hairStyle = HAIR_STYLES[state.hair_style];

  if (SPLIT_HAIRS.includes(hairStyle)) {
    layers.hairBack.src  = HAIR_PATH + hairColor + "/" + hairStyle + "_back.png";
    layers.hairFront.src = HAIR_PATH + hairColor + "/" + hairStyle + "_front.png";
  } else {
    layers.hairBack.src  = "";
    layers.hairFront.src = HAIR_PATH + hairColor + "/" + hairStyle + ".png";
  }

  // outfit
  layers.outfit.src = OUTFIT_PATHS[state.cat_idx] + OUTFITS[state.cat_idx][state.outfit_idx];

  // update labels
  document.getElementById("category-label").textContent = "Category: " + CATEGORIES[state.cat_idx];
  document.getElementById("outfit-label").textContent   = "Outfit: "   + OUTFITS[state.cat_idx][state.outfit_idx].replace(".png", "");
}

// ── CYCLE FUNCTION ──

function cycle(attr) {
  if (attr === "cat_idx") {
    state.cat_idx = (state.cat_idx + 1) % CATEGORIES.length;
    state.outfit_idx = 0; // reset outfit when category changes
  } else if (attr === "outfit_idx") {
    state.outfit_idx = (state.outfit_idx + 1) % OUTFITS[state.cat_idx].length;
  } else if (attr === "skin_idx") {
    state.skin_idx = (state.skin_idx + 1) % SKINS.length;
  } else if (attr === "hair_style") {
    state.hair_style = (state.hair_style + 1) % HAIR_STYLES.length;
  } else if (attr === "hair_color") {
    state.hair_color = (state.hair_color + 1) % HAIR_COLORS.length;
  } else if (attr === "nose_idx") {
    state.nose_idx = (state.nose_idx + 1) % NOSE_SHAPES.length;
  } else if (attr === "lip_shape") {
    state.lip_shape = (state.lip_shape + 1) % LIP_SHAPES.length;
  } else if (attr === "lip_color") {
    state.lip_color = (state.lip_color + 1) % LIP_COLORS.length;
  } else if (attr === "eye_shape") {
    state.eye_shape = (state.eye_shape + 1) % EYE_SHAPES.length;
  } else if (attr === "eye_color") {
    state.eye_color = (state.eye_color + 1) % EYE_COLORS.length;
  } else if (attr === "brow_style") {
    state.brow_style = (state.brow_style + 1) % BROW_STYLES.length;
  } else if (attr === "tattoo_idx") {
    state.tattoo_idx = (state.tattoo_idx + 1) % TATTOOS.length;
  }

  reloadLayers();
}

// ── BUTTON LISTENERS ──

// cycle buttons (left + right panels)
document.querySelectorAll(".cycle-btn").forEach(btn => {
  btn.addEventListener("click", () => {
    cycle(btn.dataset.action);
  });
});

// start button → show customizer
document.getElementById("start-btn").addEventListener("click", () => {
  mainMenu.classList.add("hidden");
  customizer.classList.remove("hidden");
  reloadLayers(); // load default character on first open
});

