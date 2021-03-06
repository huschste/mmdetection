"""DEEPSCORES

Provides access to the DEEPSCORES database with a COCO-like interface. The
only changes made compared to the coco.py file are the class labels.

Author:
    Yvan Satyawan <y_satyawan@hotmail.com>

Created on:
    November 23, 2019
"""
from .coco import *
import os

@DATASETS.register_module
class DeepScoresDataset(CocoDataset):

    CLASSES = ('brace', 'repeatDot', 'segno', 'coda', 'gClef', 'cClefAlto',
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

    def load_annotations(self, ann_file):
        img_infos = super().load_annotations(ann_file)
        DeepScoresDataset.CLASSES = tuple([self.coco.cats[x]['name'] for x in self.coco.cats])
        # f_classes = os.path.join(os.path.dirname(ann_file), "class_names.csv")
        # if os.path.exists(f_classes):
        #     import csv
        #     classes = []
        #     with open(f_classes, 'rt') as csv_classes:
        #         reader = csv.reader(csv_classes)
        #         for row in reader:
        #             classes.append(row[1])
        #     DeepScoresDataset.CLASSES = tuple(classes)
        # else:
        #     print("falling back to default class names")

        return img_infos