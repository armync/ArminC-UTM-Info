namespace Aplicatie2
{
    public partial class Meniu : Form
    {
        public Meniu()
        {
            InitializeComponent();
        }

        private void btnCalculator_Click(object sender, EventArgs e)
        {
            Calculator calc = new();
            calc.Show();
            this.Hide();
        }

        private void btnConversie_Click(object sender, EventArgs e)
        {
            Conversie conv = new();
            conv.Show();
            this.Hide();
        }

        private void btn3_Click(object sender, EventArgs e)
        {
            btn3.Text = "Apasat";
            btn3.Location = new Point(20, 10);
        }

        private void btn4_Click(object sender, EventArgs e)
        {
            this.BackColor = Color.Red;
        }
    }
}
