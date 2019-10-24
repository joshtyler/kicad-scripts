import pcbnew

def SetRefSize(SizeMM,ThicknessMM):
    board = pcbnew.GetBoard()

    for module in board.GetModules():
        module.Reference().SetTextSize(pcbnew.wxSize(pcbnew.FromMM(SizeMM),pcbnew.FromMM(SizeMM)))
        module.Reference().SetThickness(pcbnew.FromMM(ThicknessMM))