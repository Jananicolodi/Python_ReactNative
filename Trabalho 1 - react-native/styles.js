
import React from 'react'
import { StyleSheet, Dimensions } from 'react-native'
var { height, width } = Dimensions.get('window')

const styles = StyleSheet.create(

    {
        body: {
            flex: 1,
            backgroundColor: '#088A68'
        },
        imagem: {
            marginTop: 0.01 * height,
            height: 0.30 * height,
            width: 0.25 * width,
            marginHorizontal: 0.005 * width,
            marginVertical: 0.02 * height,
            borderColor: '#0B3B2E',
            borderWidth: 1
        },
        container: {
            marginTop: 0.1 * height,
            backgroundColor: '#01DFA5'

        },
        input: {
            marginTop: 0.01 * height,
            flex: 1,
            backgroundColor: "#CEF6CE",
            borderRadius: 5,
            marginHorizontal: 0.02 * width,
            height: 0.13 * height,
            textAlign: 'center',
            fontSize: 20,
            paddingRight: 10,
            marginBottom: 0.05 * height,
            borderColor: '#088A68',
            borderWidth: 1

        },
        row: {
            flexDirection: 'row'
        },
        button: {
            flex: 1,
            backgroundColor: '#039E6A',
            justifyContent: 'center',
            alignItems: 'center',
            borderRadius: 5,
            marginHorizontal: 0.02 * width,
            marginVertical: 0.01 * height,
            height: 0.1 * height,
            borderColor: '#0B3B2E',
            borderWidth: 1
            
        },
        row: {
            flexDirection: 'row'
        }
    }
)
export { styles }