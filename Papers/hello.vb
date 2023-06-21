Imports System.Windows.Forms

Public Class SumaForm
    Inherits Form

    Private label1 As Label
    Private textBox1 As TextBox
    Private label2 As Label
    Private textBox2 As TextBox
    Private button1 As Button
    Private label3 As Label

    Public Sub New()
        label1 = New Label()
        label1.Text = "Número 1:"
        label1.Location = New Point(10, 10)

        textBox1 = New TextBox()
        textBox1.Location = New Point(80, 10)

        label2 = New Label()
        label2.Text = "Número 2:"
        label2.Location = New Point(10, 40)

        textBox2 = New TextBox()
        textBox2.Location = New Point(80, 40)

        button1 = New Button()
        button1.Text = "Sumar"
        button1.Location = New Point(80, 70)
        AddHandler button1.Click, AddressOf Button1_Click

        label3 = New Label()
        label3.Text = "Resultado:"
        label3.Location = New Point(10, 100)

        Controls.Add(label1)
        Controls.Add(textBox1)
        Controls.Add(label2)
        Controls.Add(textBox2)
        Controls.Add(button1)
        Controls.Add(label3)
    End Sub

    Private Sub Button1_Click(sender As Object, e As EventArgs)
        Dim num1 As Integer
        Dim num2 As Integer
        If Integer.TryParse(textBox1.Text, num1) AndAlso Integer.TryParse(textBox2.Text, num2) Then
            Dim resultado As Integer = num1 + num2
            label3.Text = "Resultado: " & resultado.ToString()
        Else
            label3.Text = "Ingrese números válidos."
        End If
    End Sub

    Public Shared Sub Main()
        Application.Run(New SumaForm())
    End Sub
End Class
