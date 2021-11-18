import React, { Component } from 'react'
import { View, Text, H1, Image } from 'react-native'

import { styles } from './styles'
import { Button } from './Button'
import { Input } from './Input'
import { Imagem } from './img'


export default class App extends Component {

  constructor(props) {
    super(props)
    estacao= ""
    this.state = {
     estacao: ""
   } 
  }

  addEstacao = estacao => {
           console.log("estacao")    
    this.setState({
      estacao: estacao.toString()
    })
  }
    limpaTela = () => {
      this.setState({
      estacao: ""    
      })
    }
  render() {
    return (
      <View style={styles.body}>
      <View style={styles.container}>      
        <View style={styles.row}>
            <Input texto="Digite o texto"/>
          </View>            
          <View style={styles.row}>
            <Input estacao={this.state.estacao} texto="Selecione a imagem"/>
          </View>            
          <View style={styles.row}>
            <Button texto="Limpar" pressionado={() => this.limpaTela()}/>
          </View>
          <View style={styles.row}>
            <Imagem style={styles.imagem} pressionado={() => this.addEstacao("Outono")} source={{ uri: 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQAst6rG7vzULssfL4tCweFpwmpHC3GbD_6ojdIWeJEFsHP1V4Q&usqp=CAU' }}/>
            <Imagem style={styles.imagem} pressionado={() => this.addEstacao("Inverno")} source={{uri: 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcT08WRzT3dvInV07XmsrAzYERO9JyEAV7iP6gboCHspsUYC431u&usqp=CAU'}}/>
            <Imagem style={styles.imagem} pressionado={() => this.addEstacao("Primavera")} source={{uri: 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRB-wniVmRUdjsP4IK7PGPN7-pM1mKkeJ3S8qRuO8BUJKvpPR4r&usqp=CAU'}} pressionado={() => this.addEstacao("Primavera")} />             
            <Imagem style={styles.imagem} pressionado={() => this.addEstacao("Verão")} source={{ uri: 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcT68XBeQ3H1y0QJr0ZD7EkBjwXe2BFboTzfdxYe9ZizrYhKZz1s&usqp=CAU' }}/>
          </View>
        </View>
      </View>
    ) 
  }
}