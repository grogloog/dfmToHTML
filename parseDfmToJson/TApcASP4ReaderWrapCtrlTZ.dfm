object TFormFromStream: TTFormFromStream
  Left = 0
  Top = 0
  Caption = 'frmCtrlTZ'
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
    HelpContext = 6675
    BevelOuter = bvNone
    TabOrder = 0
    object lblCtrlTimeZone: TLabel
      Left = 8
      Top = 16
      Width = 84
      Height = 13
      Caption = '// lblCtrlTimeZone'
    end
    object cbCtrlTimeZone: TComboBox
      Left = 152
      Top = 13
      Width = 185
      Height = 21
      TabOrder = 0
    end
    object GroupBox1: TGroupBox
      Left = 8
      Top = 40
      Width = 329
      Height = 65
      TabOrder = 1
      object lblTZEndMode: TLabel
        Left = 8
        Top = 38
        Width = 77
        Height = 13
        Caption = '// lblTZEndMode'
      end
      object lblTZStartMode: TLabel
        Left = 8
        Top = 11
        Width = 83
        Height = 13
        Caption = '// lblTZStartMode'
      end
      object cbTZStartMode: TComboBox
        Left = 156
        Top = 8
        Width = 165
        Height = 21
        TabOrder = 0
      end
      object cbTZEndMode: TComboBox
        Left = 156
        Top = 35
        Width = 165
        Height = 21
        TabOrder = 1
      end
    end
    object gbAdditional: TGroupBox
      Left = 8
      Top = 110
      Width = 329
      Height = 91
      Caption = '// Additional'
      TabOrder = 2
      object chkBoxEnableHeldOpenAlarm: TCheckBox
        Left = 8
        Top = 22
        Width = 241
        Height = 17
        Caption = '// chkBoxEnableHeldOpenAlarm'
        TabOrder = 0
      end
      object chkBoxDisableKeyEcho: TCheckBox
        Left = 8
        Top = 43
        Width = 241
        Height = 17
        Caption = '// chkBoxDisableKeyEcho'
        TabOrder = 1
      end
      object chkBoxEnableOneWireLED: TCheckBox
        Left = 8
        Top = 64
        Width = 225
        Height = 17
        Caption = '// chkBoxEnableOneWireLED'
        TabOrder = 2
      end
    end
    object chkBoxDisableAccessPointCtrl: TCheckBox
      Left = 16
      Top = 254
      Width = 270
      Height = 17
      Caption = '// chkBoxDisableAccessPointCtrl'
      TabOrder = 3
    end
  end
end