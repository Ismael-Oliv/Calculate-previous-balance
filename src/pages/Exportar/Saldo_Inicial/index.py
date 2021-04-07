from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QProgressBar,
    QDockWidget,
    QLabel,
    QFrame,
    QPushButton,
    QToolButton,
    QDialogButtonBox
    )

from src.pages.Exportar.Saldo_Inicial.services.index import ProcessarSaldoInicial
from src.database.repository.index import dabaseRepository

def SaldoInicialFeature(Screen, ActiveCNPJ):

    def SaveButtonClicked(Barra_Progesso):
        Barra_Progesso.setValue(0)

        connection = dabaseRepository.createConection()
        Origem = TXTOrigem.text()
        Destino = TXTDestino.text()
        cnpj = ActiveCNPJ.text()
        Params = {
            'conn': connection,
            'Origem': Origem,
            'Destino':Destino,
            'CompanyName': cnpj, 
            'Barra_Progresso': Barra_Progesso,
            'Screen': Screen
            }

        response = ProcessarSaldoInicial(Params)
        print('processo concluido')

    def CancellButtonClicked():
       pass


    Screen.setGeometry(5, 20, 590, 300)
    Screen.setFixedSize(590, 300)

    Frame = Screen.frame = QFrame(Screen)
    Frame.setGeometry(15,20,560,240)
    Frame.setFrameShape(QFrame.StyledPanel)

   # Label descrição da tela
    # =======================================================
    LabelDescricao = Screen.LabelDescricao = QLabel(Frame)
    LabelDescricao.setGeometry(200,10,400,17)
    LabelDescricao.setText('Exportar - Saldo Inicial')
    # =======================================================
    
    LabelOrigem = Screen.labelOrigem = QLabel(Frame)
    LabelOrigem.setGeometry(50,50,67,17)
    LabelOrigem.setText('Origem:')

    TXTOrigem = Screen.txtOrigem = QLabel(Frame)
    TXTOrigem.setGeometry(130,50,321,17)
    TXTOrigem.setStyleSheet("""
            background-color: rgb(186, 189, 182);
    """)

    SelectPathButton = Screen.SelectPathButton = QPushButton(Frame)
    SelectPathButton.setGeometry(460, 45, 30, 30)
    SelectPathButton.setText('...')
    SelectPathButton.clicked.connect(lambda: SelectPath(TXTOrigem))

    # =============================================================
    # ================ TXT Destino
    # =============================================================
    LabelDestino = Screen.labelDestino = QLabel(Frame)
    LabelDestino.setGeometry(50,80,67,17)
    LabelDestino.setText('Destino:')

    TXTDestino = Screen.txtDestino = QLabel(Frame)
    TXTDestino.setGeometry(130,80,321,17)
    TXTDestino.setStyleSheet("""
            background-color: rgb(186, 189, 182);
    """)

    SelectDestPath = Screen.SelectDestPath = QPushButton(Frame)
    SelectDestPath.setGeometry(460, 75, 30, 30)
    SelectDestPath.setText('...')
    SelectDestPath.clicked.connect(lambda: selectDestPath(TXTDestino))


    # ==================================================
    # Status Bar
    Barra_Progesso = Screen.Barra_Progesso = QProgressBar(Frame)
    Barra_Progesso.setGeometry(130,110,321,25)

    # ==================================================

    SaveButton = Screen.saveButton = QPushButton(Frame)
    SaveButton.setGeometry(140,150,101,31)
    SaveButton.setText('Importar')
    SaveButton.clicked.connect(lambda: SaveButtonClicked(Barra_Progesso))

    CancellButton = Screen.cancellbutton = QPushButton(Frame)
    CancellButton.setGeometry(300,150,101,31)
    CancellButton.setText('Cancelar')
    CancellButton.clicked.connect(CancellButtonClicked)


    Screen.show()
