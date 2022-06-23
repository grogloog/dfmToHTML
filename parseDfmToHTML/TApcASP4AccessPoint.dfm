object TFormFromStream: TTFormFromStream
  Left = 0
  Top = 0
  Caption = 'frmAccPoint'
  ClientHeight = 373
  ClientWidth = 347
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'Tahoma'
  Font.Style = []
  OldCreateOrder = False
  PixelsPerInch = 96
  TextHeight = 13
  object pnlExport: TPanel
    Left = 0
    Top = 0
    Width = 347
    Height = 373
    HelpContext = 6528
    BevelOuter = bvNone
    TabOrder = 0
    object lblAccPointNumber: TLabel
      Left = 8
      Top = 16
      Width = 96
      Height = 13
      Caption = '// AccPoint Number:'
    end
    object Bevel1: TBevel
      Left = 8
      Top = 38
      Width = 329
      Height = 2
    end
    object lblInitMode: TLabel
      Left = 8
      Top = 51
      Width = 60
      Height = 13
      Caption = '// Init mode:'
    end
    object clEditAccPointNumber: TRxCalcEdit
      Left = 130
      Top = 13
      Width = 199
      Height = 18
      Margins.Top = 0
      TabStop = False
      Alignment = taLeftJustify
      AutoSize = False
      BorderStyle = bsNone
      Color = clBtnFace
      ButtonWidth = 0
      NumGlyphs = 2
      TabOrder = 5
      ZeroEmpty = False
    end
    object cbxInitMode: TComboBox
      Left = 176
      Top = 48
      Width = 153
      Height = 21
      ItemHeight = 13
      TabOrder = 0
    end
    object gbAPBSettings: TGroupBox
      Left = 8
      Top = 72
      Width = 329
      Height = 73
      Caption = '// APB Settings'
      TabOrder = 1
      object lblZone1: TLabel
        Left = 8
        Top = 20
        Width = 48
        Height = 13
        Caption = '// Zone 1:'
      end
      object lblZone2: TLabel
        Left = 8
        Top = 43
        Width = 48
        Height = 13
        Caption = '// Zone 2:'
      end
      object cbxZone1: TComboBox
        Left = 168
        Top = 17
        Width = 153
        Height = 21
        ItemHeight = 13
        TabOrder = 0
      end
      object cbxZone2: TComboBox
        Left = 168
        Top = 40
        Width = 153
        Height = 21
        ItemHeight = 13
        TabOrder = 1
      end
    end
    object gbStdTimeSettings: TGroupBox
      Left = 8
      Top = 151
      Width = 161
      Height = 74
      Caption = '//Standart time settings'
      TabOrder = 2
      object lblShortStrTm: TLabel
        Left = 8
        Top = 23
        Width = 86
        Height = 13
        Caption = '// ShortStrikeTime'
      end
      object lblShortHeldTm: TLabel
        Left = 8
        Top = 46
        Width = 106
        Height = 13
        Caption = '// ShortHeldOpenTime'
      end
      object clEditShortStrTm: TRxCalcEdit
        Left = 122
        Top = 20
        Width = 33
        Height = 21
        Margins.Left = 4
        Margins.Top = 1
        Alignment = taLeftJustify
        ButtonWidth = 0
        NumGlyphs = 2
        TabOrder = 0
        ZeroEmpty = False
      end
      object clEditShortHeldTm: TRxCalcEdit
        Left = 122
        Top = 43
        Width = 33
        Height = 21
        Margins.Left = 4
        Margins.Top = 1
        Alignment = taLeftJustify
        ButtonWidth = 0
        NumGlyphs = 2
        TabOrder = 1
        ZeroEmpty = False
      end
    end
    object gbAltTimeSettings: TGroupBox
      Left = 176
      Top = 151
      Width = 161
      Height = 74
      Caption = '//Alternative time settings'
      TabOrder = 3
      object lblLongStrTm: TLabel
        Left = 8
        Top = 23
        Width = 83
        Height = 13
        Caption = '// LongStrikeTime'
      end
      object lblLongHelpTm: TLabel
        Left = 8
        Top = 46
        Width = 103
        Height = 13
        Caption = '// LongHelpOpenTime'
      end
      object clEditLongStrTime: TRxCalcEdit
        Left = 122
        Top = 20
        Width = 33
        Height = 21
        Margins.Left = 4
        Margins.Top = 1
        Alignment = taLeftJustify
        ButtonWidth = 0
        NumGlyphs = 2
        TabOrder = 0
        ZeroEmpty = False
      end
      object clEditLongHeldTm: TRxCalcEdit
        Left = 122
        Top = 43
        Width = 33
        Height = 21
        Margins.Left = 4
        Margins.Top = 1
        Alignment = taLeftJustify
        ButtonWidth = 0
        NumGlyphs = 2
        TabOrder = 1
        ZeroEmpty = False
      end
    end
    object gbMask: TGroupBox
      Left = 8
      Top = 231
      Width = 329
      Height = 72
      Caption = '// mask'
      TabOrder = 4
      object chkBoxHeldOpen: TCheckBox
        Left = 8
        Top = 20
        Width = 289
        Height = 17
        Caption = 'mask HeldOpen alarms'
        TabOrder = 0
      end
      object chkBoxForcedOpen: TCheckBox
        Left = 8
        Top = 43
        Width = 289
        Height = 17
        Caption = 'mask ForcedOpen alarms'
        TabOrder = 1
      end
    end
  end
end