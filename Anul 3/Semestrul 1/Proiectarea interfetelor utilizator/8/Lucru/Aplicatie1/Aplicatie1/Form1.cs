namespace Aplicatie1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            String name = txtName.Text;
            String address = txtAddress.Text;
            MessageBox.Show(name + " " + address);
        }

        private void lstCity_SelectedIndexChanged(object sender, EventArgs e)
        {
            string text = lstCity.GetItemText(lstCity.SelectedItem);
            MessageBox.Show(text);
        }

        private void treeView1_AfterSelect(object sender, TreeViewEventArgs e)
        {

        }

        private void btnNext_Click(object sender, EventArgs e)
        {
            Form2 next1 = new Form2();
            this.Hide();
            next1.Show();
        }
    }
}
