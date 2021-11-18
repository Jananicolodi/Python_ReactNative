import { styles } from './styles'
import React, { Component } from 'react'
import { Text, Image, TouchableHighlight } from 'react-native'
function Button(props) {
    return (
        <TouchableHighlight style={styles.button} onPress={props.pressionado} underlayColor="abc">
            <Text>{props.texto}</Text>    
        </TouchableHighlight>
    )
}
export { Button }