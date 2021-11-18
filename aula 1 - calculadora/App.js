import React, { Component } from 'react'
import { View, Text } from 'react-native'

import { styles } from './styles'
import { Button } from './Button'
import { ScreenCalc } from './ScreenCalc'

export default class App extends Component {

  constructor(props) {
    super(props)
    operadores = []
    operandos = []
    operando = ""
    expr = ""
    lastDig = ""
    this.state = {
      num: ""
    }
  }

  limpaTela = () => {
    expr = ""
    this.setState({
      num: expr
    })
    operadores = []
    operandos = []
    operando = ""
  }

  isOperator = dig => {
    if (dig == "/" || dig == "*" || dig == "+" || dig == "-") {
      return true;
    }
    return false;
  }

  calcResult = () => {
    index = 1
    res = parseFloat(operandos[0])
    for (i = 0; i < operadores.length; i++) {
      op = operadores[i]
      switch (op) {
        case '+':
          res = res + parseFloat(operandos[index])
          break
        case '-':
          res = res - parseFloat(operandos[index])
          break
        case '*':
          res = res * parseFloat(operandos[index])
          break
        case '/':
          res = res / parseFloat(operandos[index])
          break
      }
      index++
    }
    this.setState({
      num: res.toString()
    })
  }

  result = () => {
    operandos.push(operando)
    operando = ""
    this.calcResult()
    console.log(operandos)
    console.log(operadores)
  }

  addDigit = dig => {
    if (this.isOperator(dig)) {
      // digito é um operador

      if (this.isOperator(lastDig)) {

        expr = expr.slice(0, -1) // remove o último caracter
      } else {
        if (operando != "") {
          operandos.push(operando)
          operando = ""
        }
      }
    } else {
      // digito é um operando (número)
      if (this.isOperator(lastDig)) { // 98 + 4
        operadores.push(lastDig)
      }
      operando += dig
    }
    lastDig = dig
    expr = expr + dig
    this.setState({
      num: expr
    })
  }

  render() {
    return (
      <View style={styles.body}>
        <View style={styles.container}>
          <View style={styles.row}>
            <ScreenCalc valor={this.state.num} />
          </View>
          <View style={styles.row}>
            <Button numero='LIMPAR' pressionado={() => this.limpaTela()} />
          </View>
          <View style={styles.row}>
            <Button numero='7' pressionado={() => this.addDigit("7")} />
            <Button numero='8' pressionado={() => this.addDigit("8")} />
            <Button numero='9' pressionado={() => this.addDigit("9")} />
            <Button numero='/' pressionado={() => this.addDigit('/')} />
          </View>
          <View style={styles.row}>
            <Button numero='4' pressionado={() => this.addDigit("4")} />
            <Button numero='5' pressionado={() => this.addDigit("5")} />
            <Button numero='6' pressionado={() => this.addDigit("6")} />
            <Button numero='*' pressionado={() => this.addDigit("*")} />
          </View>
          <View style={styles.row}>
            <Button numero='1' pressionado={() => this.addDigit("1")} />
            <Button numero='2' pressionado={() => this.addDigit("2")} />
            <Button numero='3' pressionado={() => this.addDigit("3")} />
            <Button numero='+' pressionado={() => this.addDigit("+")} />
          </View>
          <View style={styles.row}>
            <Button numero='=' pressionado={() => this.result()} />
            <Button numero='0' pressionado={() => this.addDigit("0")} />
            <Button numero='.' pressionado={() => this.addDigit(".")} />
            <Button numero='-' pressionado={() => this.addDigit("-")} />
          </View>
        </View>
      </View>
    )
  }
}