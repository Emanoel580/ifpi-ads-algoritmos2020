def main():
    hora = int(input('Número de horas: '))
    valor = float(input('Valor ganho por hora: '))
    pagamento(hora, valor)


def pagamento(hr, val):
    salario_bruto = hr * val
    inss = salario_bruto * 0.10
    ir_5 = salario_bruto * 0.05
    ir_10 = salario_bruto * 0.10
    ir_20 = salario_bruto * 0.20
    fgts = salario_bruto * 0.11
    if salario_bruto <= 900:
        salario_liquido = salario_bruto - inss
        print('SALÁRIO BRUTO: R$ {:.2f}'.format(salario_bruto))
        print('(-) IMPOSTO DE RENDA: Isento')
        print('(-) INSS: R$ {:.2f}'.format(inss))
        print('FGTS: R$ {:.2f}'.format(fgts))
        print('IMPOSTOS: R$ {:.2f}'.format(inss))
        print('SALÁRIO LÍQUIDO: R$ {:.2f}'.format(salario_liquido))
    elif 900 < salario_bruto <= 1500:
        impostos = ir_5 + inss
        salario_liquido = salario_bruto - impostos
        print('SALÁRIO BRUTO: R$ {:.2f}'.format(salario_bruto))
        print('(-) IMPOSTO DE RENDA: 5%')
        print('(-) INSS: R$ {:.2f}'.format(inss))
        print('FGTS: R$ {:.2f}'.format(fgts))
        print('IMPOSTOS: R$ {:.2f}'.format(impostos))
        print('SALÁRIO LÍQUIDO: R$ {:.2f}'.format(salario_liquido))
    elif 1500 < salario_bruto <= 2500:
        impostos = ir_10 + inss
        salario_liquido = salario_bruto - impostos
        print('SALÁRIO BRUTO: R$ {:.2f}'.format(salario_bruto))
        print('(-) IMPOSTO DE RENDA: 10%')
        print('(-) INSS: R$ {:.2f}'.format(inss))
        print('FGTS: R$ {:.2f}'.format(fgts))
        print('IMPOSTOS: R$ {:.2f}'.format(impostos))
        print('SALÁRIO LÍQUIDO: R$ {:.2f}'.format(salario_liquido))
    else:
        impostos = ir_20 + inss
        salario_liquido = salario_bruto - impostos
        print('SALÁRIO BRUTO: R$ {:.2f}'.format(salario_bruto))
        print('(-) IMPOSTO DE RENDA: 20%')
        print('(-) INSS: R$ {:.2f}'.format(inss))
        print('FGTS: R$ {:.2f}'.format(fgts))
        print('IMPOSTOS: R$ {:.2f}'.format(impostos))
        print('SALÁRIO LÍQUIDO: R$ {:.2f}'.format(salario_liquido))


if __name__ == '__main__':
    main()
