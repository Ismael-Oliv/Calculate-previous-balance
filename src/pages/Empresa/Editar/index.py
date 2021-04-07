from PyQt5.QtWidgets import (
    QComboBox,
    QDockWidget,
    QLabel,
    QFrame,
    QPushButton,
    QTextEdit
    )

from src.database.repository.index import dabaseRepository
from src.pages.Empresa.Editar.repository.index import EditarRepository
from src.pages.Empresa.Editar.services.index import removeCampany

def EditarFeature(Screen, ActiveCNPJ):

    def UpadateButtonClicked(TXTCNPJ, LabelStatus):
        CnpjCompany = TXTCNPJ.toPlainText()

        if CnpjCompany:

            result = CadastrarServices.createTables(CnpjCompany, NameCompany)

            if result == 'Empresa já cadastrada':
                TXTEmpresa.setText('')
                TXTCNPJ.setText('')
                LabelStatus.setText(f'Empresa {CnpjCompany} já cadastrada')

            else:
                
                TXTEmpresa.setText('')
                TXTCNPJ.setText('')
                LabelStatus.setText(f'Empresa {CnpjCompany} cadastrada com sucesso')

        else:
            
            LabelStatus.setText('Dados invalidos')

    def RemoveButtonClicked(LabelStatus, listButton):
        cnpj = listButton.currentText()
        conection = dabaseRepository.createConection()

        if cnpj:
            

            Result = EditarRepository.Remove(conection, cnpj)

            if Result:
                LabelStatus.setText('Processo concluido')

        else:

            LabelStatus.setText('Dados invalidos')


    def listCompanyName(listButton):
        conection = dabaseRepository.createConection()

        listOfCompany = EditarRepository.AllCompany(conection)
        arrListOfCompany = []

        for company in listOfCompany:
            arrListOfCompany.append(company[0])
            
        listButton.addItems(arrListOfCompany)

        conection.close()

    def listButtonChanges(TXTListEmpresa, listButton, TXTEditEmpresa, TXTEditCNPJ):
        conection = dabaseRepository.createConection()

        cnpj = listButton.currentText()
        companyName = EditarRepository.OneCompany(conection, cnpj)

        TXTListEmpresa.setText(companyName[0][1])

        TXTEditEmpresa.setText(companyName[0][1])
        TXTEditCNPJ.setText(companyName[0][0])

        conection.close()


    Screen.setGeometry(5, 20, 590, 500)
    Screen.setFixedSize(590, 500)

    Frame = Screen.frame = QFrame(Screen)
    Frame.setGeometry(15,20,560,350)
    Frame.setFrameShape(QFrame.StyledPanel)

    # =======================================================
    # Label descrição da tela
    # =======================================================
    LabelDescricao = Screen.LabelDescricao = QLabel(Frame)
    LabelDescricao.setGeometry(200,10,400,17)
    LabelDescricao.setText('Editar Cadastro - Empresa')
    # =======================================================


    # =======================================================
    # Listar dados Empresa
    # =======================================================
    LabelEmpresa = Screen.labelEmpresa = QLabel(Frame)
    LabelEmpresa.setGeometry(50,70,67,17)
    LabelEmpresa.setText('Empresa:')

    TXTListEmpresa = Screen.txtListEmpresa = QLabel(Frame)
    TXTListEmpresa.setGeometry(130,68,160,27)
    TXTListEmpresa.setStyleSheet("""background-color: rgb(186, 189, 182);""")

    LabelCNPJ = Screen.Labecnpj = QLabel(Frame)
    LabelCNPJ.setGeometry( 300, 70, 67, 17)
    LabelCNPJ.setText('CNPJ:')

    listButton = Screen.listbutton = QComboBox(Frame)
    listButton.setGeometry( 350, 68, 191, 27)
    
    # =======================================================


    # =======================================================
    # Editar Empresa

    LabelEmpresa = Screen.labelEmpresa = QLabel(Frame)
    LabelEmpresa.setGeometry(50,140, 67, 27)
    LabelEmpresa.setText('Nome:')

    TXTEditEmpresa = Screen.TXTEditEmpresa = QTextEdit(Frame)
    TXTEditEmpresa.setGeometry(130,140,321,27)
    TXTEditEmpresa.setStyleSheet("""background-color: rgb(211,211,211);""")

    LabelCNPJ = Screen.Labelcnpj = QLabel(Frame)
    LabelCNPJ.setGeometry(50,185,67,17)
    LabelCNPJ.setText('CNPJ:')

    TXTEditCNPJ = Screen.TXTEditCNPJ = QTextEdit(Frame)
    TXTEditCNPJ.setGeometry(130,180,321,27)
    TXTEditCNPJ.setStyleSheet("""background-color: rgb(211,211,211);""")

    # =======================================================
    listButton.currentTextChanged.connect(
    lambda:listButtonChanges(TXTListEmpresa, listButton, TXTEditEmpresa, TXTEditCNPJ)
    ) 
    listCompanyName(listButton)

    
    # =======================================================
    UpadateButton = Screen.UpadateButton = QPushButton(Frame)
    UpadateButton.setGeometry(165,260,101,31)
    UpadateButton.setText('Atualizar')
    UpadateButton.clicked.connect(
        lambda: UpadateButtonClicked(TXTEditCNPJ, TXTStatus)
        )

    RemoveButton = Screen.Removebutton = QPushButton(Frame)
    RemoveButton.setGeometry(325,260,101,31)
    RemoveButton.setText('Remover')
    RemoveButton.clicked.connect(lambda: RemoveButtonClicked(TXTStatus, listButton))

    TXTStatus = Screen.TXTStatus = QLabel(Frame)
    TXTStatus.setGeometry(140,300,300,27)
    TXTStatus.setText('')
    

    Screen.show()
