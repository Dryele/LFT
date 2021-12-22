from SintaxeAbstrata import *

class VisitorPrinter:
    def visitComposicaoCriarTabela(self, composicaoCriarTabela):
        composicaoCriarTabela.criarTabela.accept(self)
        print(' ')
        if composicaoCriarTabela.composicaoCriarTabela != None:
            composicaoCriarTabela.composicaoCriarTabela.accept(self)

    def visitComposicaoInserirDados(self, composicaoinserirdados):
        composicaoinserirdados.inserirDados.accept(self)
        print('  ')
        if composicaoinserirdados.composicaoInserirDados != None:
            composicaoinserirdados.composicaoInserirDados.accept(self)

    def visitCriaTabela(self, criatabela):
        print('CREATE TABLE', criatabela.ID, '(')
        criatabela.tabelacolunas.accept(self)
        print(');')

    def visitInserirDados(self, inseredados):
        print('INSERT INTO', inseredados.ID, 'VALUES (')
        inseredados.dadosinseridos.accept(self)
        print(');')

    def visitComposicaoDadosInseridos(self, composicaodadosinseridos):
        composicaodadosinseridos.literal.accept(self)
        if (composicaodadosinseridos.ComposicaoDadosInseridos != None):
            composicaodadosinseridos.ComposicaoDadosInseridos.accept(self)

    def visitTipoInt(self, tipoint):
        print('int')

    def visitTipoVarchar(self, tipovarchar):
        print('varchar(', tipovarchar.numInteiro, ')')

    def visitNumInteiro(self, numinteiro):
        print(numinteiro.numInteiro)

    def visitString(self, string):
        print(string.String)

    def visitDeclareVar(self, declarevar):
        print('declare ', end=' ')
        declarevar.listtypedid.accept(self)

    def visitSufixoNotNull(self, sufixo):
        print('Not NULL')

    def visitSufixoNull(self, sufixo):
        print('NULL')

    def visitSufixoNotNullPrimaryKey(self, sufixo):
        print('Not NULL Primary Key')

    def visitIf(self, ifcomando):
        print('IF', ifcomando.ID, '=')
        ifcomando.literal.accept(self)
        if (ifcomando.begin != None):
            ifcomando.begin.accept(self)
        if (ifcomando.comando != None):
            ifcomando.comando.accept(self)

    def visitIfElif(self, ifelif):
        print('IF', ifelif.IDIf, '=')
        ifelif.literalIf.accept(self)
        if (ifelif.beginIf != None):
            ifelif.beginIf.accept(self)
        if (ifelif.comandoIf != None):
            ifelif.comandoIf.accept(self)

        print('ELIF', ifelif.IDElif, '=')
        ifelif.literalElif.accept(self)
        if (ifelif.beginElif != None):
            ifelif.beginElif.accept(self)
        if (ifelif.comandoElif != None):
            ifelif.comandoElif.accept(self)

    def visitIfElse(self, ifelse):
        print('IF', ifelse.IDIf, '=')
        ifelse.literalIf.accept(self)
        if (ifelse.beginIf != None):
            ifelse.beginIf.accept(self)
        if (ifelse.comandoIf != None):
            ifelse.comandoIf.accept(self)

        print('ELSE')
        if (ifelse.beginElse != None):
            ifelse.beginElse.accept(self)
        if (ifelse.comandoElse != None):
            ifelse.comandoElse.accept(self)

    def visitDeallocate(self, deallocate):
        print('deallocate', deallocate.ID)

    def visitWhile(self, whilevist):
        print('while (', whilevist.ID, ')')
        whilevist.comandos.accept(self)

    def visitBegin(self, beginvist):
        print('begin', end='')
        beginvist.comandos.accept(self)
        print('end')

    def visitBeginSet(self, beginset):
        print('begin ', end='')
        beginset.set.accept(self)
        beginset.comandos.accept(self)
        print('end')

    def visitProcedure(self, procedure):
        print('create or alter procedure', procedure.ID, 'as begin')
        procedure.comandos.accept(self)
        print('\n')
        procedure.close.accept(self)
        print('\n')
        procedure.deallocate.accept(self)
        print('end')

    def visitOpen(self, open):
        print('open', open.ID)

    def visitClose(self, closevist):
        print('close', closevist.ID)

    def visitFetch(self, fetch):
        print('fetch', fetch.ID, 'into')
        fetch.dadossemtipo.accept(self)

    def visitSet(self, setvist):
        print('set', setvist.ID, '(')
        setvist.select.accept(self)
        print(')')

    def visitExec(self, execvist):
        print('exec', execvist.ID)
        execvist.dadossemtipo.accept(self)
        print('output')

    def visitNumFloat(self, nfloat):
        print(nfloat.numfloat)

    def visitComandos(self, comandos):
        comandos.comando.accept(self)

    def visitComandosComandos(self, comandovist):
        comandovist.comando.accept(self)
        comandovist.comandos.accept(self)

    def visitComposicaoDadosSemTipo(composicaodadossemtipo):
        print(composicaodadossemtipo.ID)
        if (composicaodadossemtipo.ComposicaoDadosSemTipo != None):
            composicaodadossemtipo.ComposicaoDadosSemTipo.accept(self)

    def visitSelectMul(self, selectmul):
        print('select mul from ', selectmul.ID)

    def visitSelectSum(self, selectsum):
        print('select sum ( ', selectsum.ID1, ')')
        print('from ', selectsum.ID2)
        print('where ', selectsum.ID3)
        print(selectsum.ID4)

    def visitSelectTypedId(self, selecttype):
        print('select ', end='')
        selecttype.listtypedid.accept(self)
        print('from ', selecttype.ID)

    def visitListTypeIdSimples(self, listtypeidsimples):
        print(listtypeidsimples.ID)
        listtypeidsimples.tipo.accept(self)

    def visitListTypeIdComposto(self, listtypeidcomposto):
        print(listtypeidcomposto.ID)
        listtypeidcomposto.tipo.accept(self)
        listtypeidcomposto.listtypeid.accept(self)

    def visitTabelaColunasSimples(self, tabelacolunassimples):
        print(tabelacolunassimples.ID)
        tabelacolunassimples.tipo.accept(self)
        if (tabelacolunassimples.sufixotable != None):
            tabelacolunassimples.sufixotable.accept(self)

    def visitTabelaColunasComposta(self, tabelacolunascomposta):
        print(tabelacolunascomposta.ID)
        tabelacolunascomposta.tipo.accept(self)
        if (tabelacolunascomposta.sufixotable != None):
            tabelacolunascomposta.sufixotable.accept(self)
        tabelacolunascomposta.tabelacolunas.accept(self)

    def visitTipoNumeric(self, tiponumeric):
        print('numeric')

    def visitTipoDateTime(self, tipodatetime):
        print('datetime')

    def visitTipoNumFloat(self, tiponumfloat):
        print('numfloat')
