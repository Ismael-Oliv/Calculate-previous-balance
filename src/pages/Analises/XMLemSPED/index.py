from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QShowEvent, QActionEvent

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
from src.pages.Analises.XMLemSPED.services.index import VerificarXMLInSped

def XMLInSPEDFeature(Screen, ActiveCNPJ):

    def CloseEvent(Event):

        TXTStatus.setText('')
        TXTOrigem.setText('')
        TXTDestino.setText('')


    def ProcessButton(Barra_Progesso):
        Barra_Progesso.setValue(0)
        TXTStatus.setText('')

        connection = dabaseRepository.createConection()
        origem = TXTOrigem.text()
        destino = TXTDestino.text()
        CompanyName = ActiveCNPJ.text()

        Params = {
            'conn': connection,
            'origem': origem,
            'destino': destino,
            'Barra_Progesso': Barra_Progesso,
            'CompanyName':CompanyName
            }

        if CompanyName:
            
            if not origem or not destino:
                TXTStatus.setText('Caminho(s) não definidos')
                return 

            response = VerificarXMLInSped(Params)

            TXTStatus.setText(response)

        else:

             TXTStatus.setText('Nenhuma empresa foi ativada')

        connection.close()

    def CancellButtonClicked():
        ActiveCompany.setText('')

    def SelectOrigemPath(TXTOrigem):
        directory = QtWidgets.QFileDialog.getExistingDirectory(
            None, 'Selecione a pasta com SPED:', '/', QtWidgets.QFileDialog.ShowDirsOnly)

        TXTOrigem.setText(directory)

    def SelectDestinoPath(TXTOrigem):
        directory = QtWidgets.QFileDialog.getExistingDirectory(
            None, 'Selecione a pasta com SPED:', '/', QtWidgets.QFileDialog.ShowDirsOnly)

        TXTOrigem.setText(directory)


    Screen.setGeometry(5, 20, 590, 320)
    Screen.setFixedSize(590, 320)

    Frame = Screen.frame = QFrame(Screen)
    Frame.setGeometry(15,20,560,280)
    Frame.setFrameShape(QFrame.StyledPanel)

    # Label descrição da tela
    # =======================================================
    LabelDescricao = Screen.LabelDescricao = QLabel(Frame)
    LabelDescricao.setGeometry(190,10,400,17)
    LabelDescricao.setText('Verificações - Verificar XMl em SPED')


    # label de Origem
    # =======================================================
    LabelOrigem = Screen.labelOrigem = QLabel(Frame)
    LabelOrigem.setGeometry(50,50,67,17)
    LabelOrigem.setText('Origem:')


    TXTOrigem = Screen.txtOrigem = QLabel(Frame)
    TXTOrigem.setGeometry(130,50,321,17)
    TXTOrigem.setStyleSheet("""background-color: rgb(186, 189, 182);""")

    SelectOriginPath = Screen.SelectOriginPath = QPushButton(Frame)
    SelectOriginPath.setGeometry(460, 45, 30, 25)
    SelectOriginPath.setText('...')
    SelectOriginPath.clicked.connect(lambda: SelectOrigemPath(TXTOrigem))

    # =======================================================

    # label de Destino
    # =======================================================
    LabelDestino = Screen.labelDestino = QLabel(Frame)
    LabelDestino.setGeometry(50, 80,67,17)
    LabelDestino.setText('Destino:')


    TXTDestino = Screen.txtDestino = QLabel(Frame)
    TXTDestino.setGeometry(130, 80,321,17)
    TXTDestino.setStyleSheet("""
            background-color: rgb(186, 189, 182);
    """)

    SelecDestinoPath = Screen.SelecDestinoPath = QPushButton(Frame)
    SelecDestinoPath.setGeometry(460, 75, 30, 25)
    SelecDestinoPath.setText('...')
    SelecDestinoPath.clicked.connect(lambda: SelectDestinoPath(TXTDestino))

    # =======================================================

    # ==================================================
    # Status Bar
    Barra_Progesso = Screen.Barra_Progesso = QProgressBar(Frame)
    Barra_Progesso.setGeometry(130,120,321,25)

    # ==================================================

    SaveButton = Screen.saveButton = QPushButton(Frame)
    SaveButton.setGeometry(170,180,101,31)
    SaveButton.setText('Importar')
    SaveButton.clicked.connect(lambda: ProcessButton(Barra_Progesso))

    CancellButton = Screen.cancellbutton = QPushButton(Frame)
    CancellButton.setGeometry(340,180,101,31)
    CancellButton.setText('Cancelar')
    CancellButton.clicked.connect(CancellButtonClicked)

    TXTStatus = Screen.TXTStatus = QLabel(Frame)
    TXTStatus.setGeometry(140,220,300,27)


    Screen.closeEvent = CloseEvent
    Screen.show()
