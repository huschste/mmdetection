"""Classes Lookup.

Lookup tables for classes from the COCO and DeepScores dataset.
"""


DEEPSCORES = ('brace', 'repeatDot', 'segno', 'coda', 'gClef', 'cClefAlto',
              'cClefTenor', 'fClef', 'unpitchedPercussionClef1', 'gClefChange',
              'cClefAltoChange', 'cClefTenorChange', 'fClefChange', 'clef8',
              'clef15', 'timeSig0', 'timeSig1', 'timeSig2', 'timeSig3',
              'timeSig4', 'timeSig5', 'timeSig6', 'timeSig7', 'timeSig8',
              'timeSig9', 'timeSig12', 'timeSig16', 'timeSigCommon',
              'timeSigCutCommon', 'noteheadBlack', 'noteheadBlackSmall',
              'noteheadHalf', 'noteheadHalfSmall', 'noteheadWhole',
              'noteheadWholeSmall', 'noteheadDoubleWhole',
              'noteheadDoubleWholeSmall', 'augmentationDot', 'flag8thUp',
              'flag8thUpSmall', 'flag16thUp', 'flag32ndUp', 'flag64thUp',
              'flag128thUp', 'flag8thDown', 'flag8thDownSmall', 'flag16thDown',
              'flag32ndDown', 'flag64thDown', 'flag128thDown',
              'accidentalFlat', 'accidentalFlatSmall', 'accidentalNatural',
              'accidentalNaturalSmall', 'accidentalSharp',
              'accidentalSharpSmall', 'accidentalDoubleSharp',
              'accidentalDoubleFlat', 'keyFlat', 'keyNatural', 'keySharp',
              'articAccentAbove', 'articAccentBelow', 'articStaccatoAbove',
              'articStaccatoBelow', 'articTenutoAbove', 'articTenutoBelow',
              'articStaccatissimoAbove', 'articStaccatissimoBelow',
              'articMarcatoAbove', 'articMarcatoBelow', 'fermataAbove',
              'fermataBelow', 'caesura', 'restMaxima', 'restLonga',
              'restDoubleWhole', 'restWhole', 'restHalf', 'restQuarter',
              'rest8th', 'rest16th', 'rest32nd', 'rest64th', 'rest128th',
              'restHBar', 'dynamicPiano', 'dynamicMezzo', 'dynamicForte',
              'dynamicPPPPP', 'dynamicPPPP', 'dynamicPPP', 'dynamicPP',
              'dynamicMP', 'dynamicMF', 'dynamicFF', 'dynamicFFF',
              'dynamicFFFF', 'dynamicFFFFF', 'dynamicFortePiano',
              'dynamicSforzando1', 'dynamicSforzato', 'dynamicRinforzando2',
              'graceNoteAcciaccaturaStemUp', 'graceNoteAppoggiaturaStemUp',
              'graceNoteAcciaccaturaStemDown', 'graceNoteAppoggiaturaStemDown',
              'ornamentTrill', 'ornamentTurn', 'ornamentTurnInverted',
              'ornamentMordent', 'stringsDownBow', 'stringsUpBow',
              'arpeggiato', 'keyboardPedalPed', 'keyboardPedalUp', 'tuplet3',
              'tuplet6', 'fingering0', 'fingering1', 'fingering2',
              'fingering3', 'fingering4', 'fingering5'
              )

CATS = [{'supercategory': 'person', 'id': 1, 'name': 'person'},
        {'supercategory': 'vehicle', 'id': 2, 'name': 'bicycle'},
        {'supercategory': 'vehicle', 'id': 3, 'name': 'car'},
        {'supercategory': 'vehicle', 'id': 4, 'name': 'motorcycle'},
        {'supercategory': 'vehicle', 'id': 5, 'name': 'airplane'},
        {'supercategory': 'vehicle', 'id': 6, 'name': 'bus'},
        {'supercategory': 'vehicle', 'id': 7, 'name': 'train'},
        {'supercategory': 'vehicle', 'id': 8, 'name': 'truck'},
        {'supercategory': 'vehicle', 'id': 9, 'name': 'boat'},
        {'supercategory': 'outdoor', 'id': 10, 'name': 'traffic light'},
        {'supercategory': 'outdoor', 'id': 11, 'name': 'fire hydrant'},
        {'supercategory': 'outdoor', 'id': 13, 'name': 'stop sign'},
        {'supercategory': 'outdoor', 'id': 14, 'name': 'parking meter'},
        {'supercategory': 'outdoor', 'id': 15, 'name': 'bench'},
        {'supercategory': 'animal', 'id': 16, 'name': 'bird'},
        {'supercategory': 'animal', 'id': 17, 'name': 'cat'},
        {'supercategory': 'animal', 'id': 18, 'name': 'dog'},
        {'supercategory': 'animal', 'id': 19, 'name': 'horse'},
        {'supercategory': 'animal', 'id': 20, 'name': 'sheep'},
        {'supercategory': 'animal', 'id': 21, 'name': 'cow'},
        {'supercategory': 'animal', 'id': 22, 'name': 'elephant'},
        {'supercategory': 'animal', 'id': 23, 'name': 'bear'},
        {'supercategory': 'animal', 'id': 24, 'name': 'zebra'},
        {'supercategory': 'animal', 'id': 25, 'name': 'giraffe'},
        {'supercategory': 'accessory', 'id': 27, 'name': 'backpack'},
        {'supercategory': 'accessory', 'id': 28, 'name': 'umbrella'},
        {'supercategory': 'accessory', 'id': 31, 'name': 'handbag'},
        {'supercategory': 'accessory', 'id': 32, 'name': 'tie'},
        {'supercategory': 'accessory', 'id': 33, 'name': 'suitcase'},
        {'supercategory': 'sports', 'id': 34, 'name': 'frisbee'},
        {'supercategory': 'sports', 'id': 35, 'name': 'skis'},
        {'supercategory': 'sports', 'id': 36, 'name': 'snowboard'},
        {'supercategory': 'sports', 'id': 37, 'name': 'sports ball'},
        {'supercategory': 'sports', 'id': 38, 'name': 'kite'},
        {'supercategory': 'sports', 'id': 39, 'name': 'baseball bat'},
        {'supercategory': 'sports', 'id': 40, 'name': 'baseball glove'},
        {'supercategory': 'sports', 'id': 41, 'name': 'skateboard'},
        {'supercategory': 'sports', 'id': 42, 'name': 'surfboard'},
        {'supercategory': 'sports', 'id': 43, 'name': 'tennis racket'},
        {'supercategory': 'kitchen', 'id': 44, 'name': 'bottle'},
        {'supercategory': 'kitchen', 'id': 46, 'name': 'wine glass'},
        {'supercategory': 'kitchen', 'id': 47, 'name': 'cup'},
        {'supercategory': 'kitchen', 'id': 48, 'name': 'fork'},
        {'supercategory': 'kitchen', 'id': 49, 'name': 'knife'},
        {'supercategory': 'kitchen', 'id': 50, 'name': 'spoon'},
        {'supercategory': 'kitchen', 'id': 51, 'name': 'bowl'},
        {'supercategory': 'food', 'id': 52, 'name': 'banana'},
        {'supercategory': 'food', 'id': 53, 'name': 'apple'},
        {'supercategory': 'food', 'id': 54, 'name': 'sandwich'},
        {'supercategory': 'food', 'id': 55, 'name': 'orange'},
        {'supercategory': 'food', 'id': 56, 'name': 'broccoli'},
        {'supercategory': 'food', 'id': 57, 'name': 'carrot'},
        {'supercategory': 'food', 'id': 58, 'name': 'hot dog'},
        {'supercategory': 'food', 'id': 59, 'name': 'pizza'},
        {'supercategory': 'food', 'id': 60, 'name': 'donut'},
        {'supercategory': 'food', 'id': 61, 'name': 'cake'},
        {'supercategory': 'furniture', 'id': 62, 'name': 'chair'},
        {'supercategory': 'furniture', 'id': 63, 'name': 'couch'},
        {'supercategory': 'furniture', 'id': 64, 'name': 'potted plant'},
        {'supercategory': 'furniture', 'id': 65, 'name': 'bed'},
        {'supercategory': 'furniture', 'id': 67, 'name': 'dining table'},
        {'supercategory': 'furniture', 'id': 70, 'name': 'toilet'},
        {'supercategory': 'electronic', 'id': 72, 'name': 'tv'},
        {'supercategory': 'electronic', 'id': 73, 'name': 'laptop'},
        {'supercategory': 'electronic', 'id': 74, 'name': 'mouse'},
        {'supercategory': 'electronic', 'id': 75, 'name': 'remote'},
        {'supercategory': 'electronic', 'id': 76, 'name': 'keyboard'},
        {'supercategory': 'electronic', 'id': 77, 'name': 'cell phone'},
        {'supercategory': 'appliance', 'id': 78, 'name': 'microwave'},
        {'supercategory': 'appliance', 'id': 79, 'name': 'oven'},
        {'supercategory': 'appliance', 'id': 80, 'name': 'toaster'},
        {'supercategory': 'appliance', 'id': 81, 'name': 'sink'},
        {'supercategory': 'appliance', 'id': 82, 'name': 'refrigerator'},
        {'supercategory': 'indoor', 'id': 84, 'name': 'book'},
        {'supercategory': 'indoor', 'id': 85, 'name': 'clock'},
        {'supercategory': 'indoor', 'id': 86, 'name': 'vase'},
        {'supercategory': 'indoor', 'id': 87, 'name': 'scissors'},
        {'supercategory': 'indoor', 'id': 88, 'name': 'teddy bear'},
        {'supercategory': 'indoor', 'id': 89, 'name': 'hair drier'},
        {'supercategory': 'indoor', 'id': 90, 'name': 'toothbrush'}]

CAT_DICT = {1: 'person',
            2: 'bicycle',
            3: 'car',
            4: 'motorcycle',
            5: 'airplane',
            6: 'bus',
            7: 'train',
            8: 'truck',
            9: 'boat',
            10: 'traffic light',
            11: 'fire hydrant',
            13: 'stop sign',
            14: 'parking meter',
            15: 'bench',
            16: 'bird',
            17: 'cat',
            18: 'dog',
            19: 'horse',
            20: 'sheep',
            21: 'cow',
            22: 'elephant',
            23: 'bear',
            24: 'zebra',
            25: 'giraffe',
            27: 'backpack',
            28: 'umbrella',
            31: 'handbag',
            32: 'tie',
            33: 'suitcase',
            34: 'frisbee',
            35: 'skis',
            36: 'snowboard',
            37: 'sports ball',
            38: 'kite',
            39: 'baseball bat',
            40: 'baseball glove',
            41: 'skateboard',
            42: 'surfboard',
            43: 'tennis racket',
            44: 'bottle',
            46: 'wine glass',
            47: 'cup',
            48: 'fork',
            49: 'knife',
            50: 'spoon',
            51: 'bowl',
            52: 'banana',
            53: 'apple',
            54: 'sandwich',
            55: 'orange',
            56: 'broccoli',
            57: 'carrot',
            58: 'hot dog',
            59: 'pizza',
            60: 'donut',
            61: 'cake',
            62: 'chair',
            63: 'couch',
            64: 'potted plant',
            65: 'bed',
            67: 'dining table',
            70: 'toilet',
            72: 'tv',
            73: 'laptop',
            74: 'mouse',
            75: 'remote',
            76: 'keyboard',
            77: 'cell phone',
            78: 'microwave',
            79: 'oven',
            80: 'toaster',
            81: 'sink',
            82: 'refrigerator',
            84: 'book',
            85: 'clock',
            86: 'vase',
            87: 'scissors',
            88: 'teddy bear',
            89: 'hair drier',
            90: 'toothbrush'}

CLASSES = ('person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus',
           'train', 'truck', 'boat', 'traffic_light', 'fire_hydrant',
           'stop_sign', 'parking_meter', 'bench', 'bird', 'cat', 'dog',
           'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe',
           'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee',
           'skis', 'snowboard', 'sports_ball', 'kite', 'baseball_bat',
           'baseball_glove', 'skateboard', 'surfboard', 'tennis_racket',
           'bottle', 'wine_glass', 'cup', 'fork', 'knife', 'spoon', 'bowl',
           'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot',
           'hot_dog', 'pizza', 'donut', 'cake', 'chair', 'couch',
           'potted_plant', 'bed', 'dining_table', 'toilet', 'tv', 'laptop',
           'mouse', 'remote', 'keyboard', 'cell_phone', 'microwave',
           'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock',
           'vase', 'scissors', 'teddy_bear', 'hair_drier', 'toothbrush')

CATEGORIES = [
        "__background",
        "person",
        "bicycle",
        "car",
        "motorcycle",
        "airplane",
        "bus",
        "train",
        "truck",
        "boat",
        "traffic light",
        "fire hydrant",
        "stop sign",
        "parking meter",
        "bench",
        "bird",
        "cat",
        "dog",
        "horse",
        "sheep",
        "cow",
        "elephant",
        "bear",
        "zebra",
        "giraffe",
        "backpack",
        "umbrella",
        "handbag",
        "tie",
        "suitcase",
        "frisbee",
        "skis",
        "snowboard",
        "sports ball",
        "kite",
        "baseball bat",
        "baseball glove",
        "skateboard",
        "surfboard",
        "tennis racket",
        "bottle",
        "wine glass",
        "cup",
        "fork",
        "knife",
        "spoon",
        "bowl",
        "banana",
        "apple",
        "sandwich",
        "orange",
        "broccoli",
        "carrot",
        "hot dog",
        "pizza",
        "donut",
        "cake",
        "chair",
        "couch",
        "potted plant",
        "bed",
        "dining table",
        "toilet",
        "tv",
        "laptop",
        "mouse",
        "remote",
        "keyboard",
        "cell phone",
        "microwave",
        "oven",
        "toaster",
        "sink",
        "refrigerator",
        "book",
        "clock",
        "vase",
        "scissors",
        "teddy bear",
        "hair drier",
        "toothbrush",
    ]