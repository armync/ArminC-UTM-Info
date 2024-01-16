using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;

namespace Aplicatie2
{
    public partial class Conversie : Form
    {
        public Conversie()
        {
            InitializeComponent();
            cbConvert.SelectedIndex = 0;
        }

        private void btnConversie_Click(object sender, EventArgs e)
        {
            string selectedItem = cbConvert.Items[cbConvert.SelectedIndex].ToString();
            double t1, t2;
            try
            {
                switch (selectedItem)
                {
                    case "Inch -> CM":
                        {
                            t1 = Convert.ToDouble(txt1.Text);
                            t2 = t1 * 2.54;
                            txt2.Text = t2.ToString("F2");
                            break;
                        }
                    case "Celsius -> Fahrenheit":
                        {
                            t1 = Convert.ToDouble(txt1.Text);
                            t2 = (t1 * 1.8) + 32;
                            txt2.Text = t2.ToString("F2");
                            break;
                        }
                    case "Mile -> KM":
                        {
                            t1 = Convert.ToDouble(txt1.Text);
                            t2 = t1 * 1.60935;
                            txt2.Text = t2.ToString("F2");
                            break;
                        }
                    case "Meter -> Yard":
                        {
                            t1 = Convert.ToDouble(txt1.Text);
                            t2 = t1 * 1.0936132983;
                            txt2.Text = t2.ToString("F2");
                            break;
                        }
                    case "Liters -> M3":
                        {
                            t1 = Convert.ToDouble(txt1.Text);
                            t2 = t1 * 0.001;
                            txt2.Text = t2.ToString("F4");
                            break;
                        }

                    default:
                        {
                            break;
                        }
                }
            }

            catch
            {
                txt2.Text = "Eroare!";
            }
        }

        private void btnReset_Click(object sender, EventArgs e)
        {
            txt1.Text = "";
            txt2.Text = "";
        }

        private void btnMeniu_Click(object sender, EventArgs e)
        {
            Meniu menu = new();
            this.Hide();
            menu.Show();
        }
    }
}