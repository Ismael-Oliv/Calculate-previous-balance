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

from src.database.repository.index import dabaseRepository
from src.pages.Importar.RegistroC170.services.index import ReadRegistroH010
from src.pages.Importar.RegistroH010.services.index import SalvarRegistroH010

def RegistroH010Feature(Screen, ActiveCNPJ):

    def SaveButtonClicked(Barra_Progesso):
        Barra_Progesso.setValue(0)

        connection = dabaseRepository.createConection()
        path = TXTOrigem.text()

        Params = {
            'Origem': path,
            'CompanyName': ActiveCNPJ,
            'Barra_Progesso': Barra_Progesso,
            'Screen': Screen
            }

        response = SalvarRegistroH010(Params)
        print('processo terminado')
        connection.close()

    def CancellButtonClicked():
        ActiveCompany.setText('')

    def SelectPath(TXTOrigem):
        directory = QtWidgets.QFileDialog.getExistingDirectory(
            None, 'Selecione a pasta com SPED:', '/', QtWidgets.QFileDialog.ShowDirsOnly)

        TXTOrigem.setText(directory)

    Screen.setGeometry(5, 20, 590, 300)
    Screen.setFixedSize(590, 300)

    Frame = Screen.frame = QFrame(Screen)
    Frame.setGeometry(15,20,560,240)
    Frame.setFrameShape(QFrame.StyledPanel)

    # Label descrição da tela
    # =======================================================
    LabelDescricao = Screen.LabelDescricao = QLabel(Frame)
    LabelDescricao.setGeometry(200,10,400,17)
    LabelDescricao.setText('Importar - Registro H010')


    # label de Origem
    # =======================================================
    LabelOrigem = Screen.labelOrigem = QLabel(Frame)
    LabelOrigem.setGeometry(50,50,67,17)
    LabelOrigem.setText('Origem:')
    # =======================================================

    TXTOrigem = Screen.txtOrigem = QLabel(Frame)
    TXTOrigem.setGeometry(130,50,321,17)
    TXTOrigem.setStyleSheet("""
            background-color: rgb(186, 189, 182);
    """)

    SelectPathButton = Screen.SelectPathButton = QPushButton(Frame)
    SelectPathButton.setGeometry(460, 45, 30, 30)
    SelectPathButton.setText('...')
    SelectPathButton.clicked.connect(lambda: SelectPath(TXTOrigem))

    # ==================================================
    # Status Bar
    Barra_Progesso = Screen.Barra_Progesso = QProgressBar(Frame)
    Barra_Progesso.setGeometry(130,90,321,25)

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
