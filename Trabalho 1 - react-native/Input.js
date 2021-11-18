import React from 'react'
import { TextInput } from 'react-native'

import { styles } from './styles'

function Input(props) {
    return (
        <TextInput style={styles.input}  value={props.estacao} placeholder={props.texto}/>

    )
}
export { Input }