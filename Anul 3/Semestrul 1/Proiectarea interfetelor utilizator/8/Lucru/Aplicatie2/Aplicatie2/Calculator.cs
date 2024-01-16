using System;
using System.Windows.Forms;
using static System.Windows.Forms.DataFormats;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;

namespace Aplicatie2
{
    public partial class Calculator : Form
    {
        public Calculator()
        {
            InitializeComponent();
            btnCalculeaza.Click += btnCalculeaza_Click;
        }

        private void btnCalculeaza_Click(object sender, EventArgs e)
        {
            string selectedItem = cbOperator.SelectedItem?.ToString();
            int result = 0;
            double rez = 1;

            try
            {
                switch (selectedItem)
                {
                    case "+":
                        {
                            result = Convert.ToInt32(txtOp1.Text) + Convert.ToInt32(txtOp2.Text);
                            txtRezultat.Text = result.ToString();
                            break;
                        }
                    case "-":
                        {
                            result = Convert.ToInt32(txtOp1.Text) - Convert.ToInt32(txtOp2.Text);
                            txtRezultat.Text = result.ToString();
                            break;
                        }
                    case "*":
                        {
                            rez = Convert.ToDouble(txtOp1.Text) * Convert.ToDouble(txtOp2.Text);
                            txtRezultat.Text = rez.ToString();
                            break;
                        }
                    case "/":
                        {
                            double op2Value = Convert.ToDouble(txtOp2.Text);

                            if (op2Value != 0)
                            {
                                rez = Convert.ToDouble(txtOp1.Text) / op2Value;
                                txtRezultat.Text = rez.ToString();
                            }
                            else
                            {
                                txtRezultat.Text = "Impartire la zero!";
                            }
                            break;
                        }
                    case "^":
                        {
                            rez = Math.Pow(Convert.ToDouble(txtOp1.Text), Convert.ToDouble(txtOp2.Text));
                            txtRezultat.Text = rez.ToString();
                            break;
                        }
                    default:
                        {
                            txtRezultat.Text = "Operator invalid!";
                            break;
                        }
                }
            }
            catch
            {
                txtRezultat.Text = "Eroare!";
            }

        }

        private void btnBack_Click(object sender, EventArgs e)
        {
            Meniu back = new();
            this.Hide();
            back.Show();
        }

        private void btnReset_Click(object sender, EventArgs e)
        {
            txtOp1.Text = "";
            txtOp2.Text = "";
            txtRezultat.Text = "";
            cbOperator.Text = "";
        }
    }
}
