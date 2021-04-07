from PyQt5.QtWidgets import (
    QComboBox,
    QDockWidget,
    QLabel,
    QFrame,
    QPushButton,
    QTextEdit
    )

from src.pages.Empresa.Cadastrar.services.index import CadastrarServices

def CadastrarFeature(Screen):

    def CloseEvent(Event):
        LabelStatus.setText('')

    def AtiveButtonClicked(TXTEmpresa, TXTCNPJ, LabelStatus):
        NameCompany = TXTEmpresa.toPlainText()
        CnpjCompany = TXTCNPJ.toPlainText()

        if NameCompany or CnpjCompany != " ":
            
            create = CadastrarServices()
            
            result = create.createTables(CnpjCompany, NameCompany)
            print(result)

            LabelStatus.setText(f'Processo concluido')

            print(result)

    def CancellButtonClicked():
        ActiveCompany.setText('')


    Screen.setGeometry(5, 20, 590, 300)
    Screen.setFixedSize(590, 300)

    Frame = Screen.frame = QFrame(Screen)
    Frame.setGeometry(15,20,560,240)
    Frame.setFrameShape(QFrame.StyledPanel)

    LabelEmpresa = Screen.labelEmpresa = QLabel(Frame)
    LabelEmpresa.setGeometry(50,50,67,17)
    LabelEmpresa.setText('Empresa:')

    TXTEmpresa = Screen.txtEmpresa = QTextEdit(Frame)
    TXTEmpresa.setGeometry(130,48,330,27)

    LabelCNPJ = Screen.Labecnpj = QLabel(Frame)
    LabelCNPJ.setGeometry(50,85,67,17)
    LabelCNPJ.setText('CNPJ:')

    # ==================================================
    # Lista de Empresas
    TXTCNPJ = Screen.listbutton = QTextEdit(Frame)
    TXTCNPJ.setGeometry(130,83,191,27)

    # ==================================================

    SaveButton = Screen.saveButton = QPushButton(Frame)
    SaveButton.setGeometry(165,150,101,31)
    SaveButton.setText('Cadastrar')
    SaveButton.clicked.connect(lambda: AtiveButtonClicked(TXTEmpresa, TXTCNPJ, LabelStatus))

    CancellButton = Screen.cancellbutton = QPushButton(Frame)
    CancellButton.setGeometry(325,150,101,31)
    CancellButton.setText('Cancelar')
    CancellButton.clicked.connect(CancellButtonClicked)

    LabelStatus = Screen.Labelstatus = QLabel(Frame)
    LabelStatus.setGeometry(160,180,341,60)


    Screen.closeEvent = CloseEvent
    Screen.show()
