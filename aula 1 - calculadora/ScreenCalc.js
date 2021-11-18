import React from 'react'
import { TextInput } from 'react-native'

import { styles } from './styles'

function ScreenCalc(props) {
    return(
        <TextInput style={styles.screen} placeholder='0' value={props.valor}></TextInput>
    )
}
export { ScreenCalc }