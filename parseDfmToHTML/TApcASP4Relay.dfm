object TFormFromStream: TTFormFromStream
  Left = 0
  Top = 0
  Caption = 'Form1'
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
    HelpContext = 6546
    TabOrder = 0
    object lblRelayNumber: TLabel
      Left = 8
      Top = 16
      Width = 81
      Height = 13
      Caption = '// Relay number:'
    end
    object Bevel1: TBevel
      Left = 8
      Top = 44
      Width = 330
      Height = 2
      Shape = bsTopLine
    end
    object lblPulseDuration: TLabel
      Left = 8
      Top = 146
      Width = 79
      Height = 13
      Caption = '// Pulse duration'
    end
    object clEditRelayNumber: TRxCalcEdit
      Left = 113
      Top = 17
      Width = 226
      Height = 18
      Margins.Top = 0
      TabStop = False
      Alignment = taLeftJustify
      AutoSize = False
      BorderStyle = bsNone
      Color = clBtnFace
      ButtonWidth = 0
      NumGlyphs = 2
      TabOrder = 2
      ZeroEmpty = False
    end
    object gbTZFlags: TGroupBox
      Left = 8
      Top = 191
      Width = 330
      Height = 105
      TabOrder = 4
      TabStop = False
      object lblControlTZ: TLabel
        Left = 8
        Top = 17
        Width = 61
        Height = 13
        Caption = '// Contol TZ:'
      end
      object chkBoxPulseAtTZStart: TCheckBox
        Left = 8
        Top = 59
        Width = 230
        Height = 17
        Caption = '// '#1055#1086#1076#1072#1074#1072#1090#1100' '#1080#1084#1087#1091#1083#1100#1089' '#1074' '#1085#1072#1095#1072#1083#1077
        TabOrder = 2
      end
      object chkBoxPulseAtTZEnd: TCheckBox
        Left = 8
        Top = 80
        Width = 230
        Height = 17
        Caption = '// '#1055#1086#1076#1072#1074#1072#1090#1100' '#1080#1084#1091#1083#1100#1089' '#1074' '#1082#1086#1085#1094#1077
        TabOrder = 3
      end
      object chkBoxTurnONWhileTZActive: TCheckBox
        Left = 8
        Top = 38
        Width = 230
        Height = 17
        Caption = '// '#1055#1086#1076#1076#1077#1088#1078#1080#1074#1072#1090#1100' '#1074#1082#1083#1102#1095#1077#1085#1085#1099#1084
        TabOrder = 1
      end
      object cbxControlTZ: TComboBox
        Left = 184
        Top = 14
        Width = 137
        Height = 21
        ItemHeight = 13
        TabOrder = 0
      end
    end
    object chkBoxConfigured: TCheckBox
      Left = 8
      Top = 52
      Width = 160
      Height = 17
      Caption = '// Configured'
      TabOrder = 0
    end
    object rdGrpInitialState: TRadioGroup
      Left = 9
      Top = 75
      Width = 330
      Height = 59
      Caption = '// rdGrpInitialState'
      TabOrder = 1
    end
    object spEditPulseDuration: TRxSpinEdit
      Left = 192
      Top = 142
      Width = 146
      Height = 21
      ButtonKind = bkStandard
      TabOrder = 2
    end
    object chkBoxRelayOffTerminatesPulse: TCheckBox
      Left = 8
      Top = 169
      Width = 230
      Height = 17
      Caption = '// '#1088#1072#1079#1088#1077#1096#1072#1090#1100' '#1087#1088#1077#1088#1099#1074#1072#1090#1100' '#1080#1084#1087#1091#1083#1100#1089
      TabOrder = 3
    end
  end
end