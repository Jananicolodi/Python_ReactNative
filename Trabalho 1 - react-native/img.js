import { styles } from './styles'
import React, { Component } from 'react'
import { Text, Image, TouchableHighlight } from 'react-native'
function Imagem(props) {
    return (
        <TouchableHighlight onPress={props.pressionado} underlayColor="abc">
            <Image style={styles.imagem} source={props.source} />
                 </TouchableHighlight>
    )
}
export { Imagem }