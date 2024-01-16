namespace Aplicatie1
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            TreeNode treeNode1 = new TreeNode("Label");
            TreeNode treeNode2 = new TreeNode("Button");
            TreeNode treeNode3 = new TreeNode("Checkbox");
            TreeNode treeNode4 = new TreeNode("Root", new TreeNode[] { treeNode1, treeNode2, treeNode3 });
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            label1 = new Label();
            groupBox1 = new GroupBox();
            txtAddress = new TextBox();
            txtName = new TextBox();
            label3 = new Label();
            label2 = new Label();
            lstCity = new ListBox();
            rdMale = new RadioButton();
            rdFemale = new RadioButton();
            chkC = new CheckBox();
            chkASP = new CheckBox();
            btnSubmit = new Button();
            treeView1 = new TreeView();
            pictureBox1 = new PictureBox();
            btnNext = new Button();
            groupBox1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)pictureBox1).BeginInit();
            SuspendLayout();
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(12, 322);
            label1.Name = "label1";
            label1.Size = new Size(70, 15);
            label1.TabIndex = 0;
            label1.Text = "Hello World";
            label1.Click += label1_Click;
            // 
            // groupBox1
            // 
            groupBox1.Controls.Add(txtAddress);
            groupBox1.Controls.Add(txtName);
            groupBox1.Controls.Add(label3);
            groupBox1.Controls.Add(label2);
            groupBox1.Location = new Point(12, 12);
            groupBox1.Name = "groupBox1";
            groupBox1.Size = new Size(200, 100);
            groupBox1.TabIndex = 1;
            groupBox1.TabStop = false;
            groupBox1.Text = "User Details";
            // 
            // txtAddress
            // 
            txtAddress.Location = new Point(68, 60);
            txtAddress.Name = "txtAddress";
            txtAddress.ScrollBars = ScrollBars.Vertical;
            txtAddress.Size = new Size(100, 23);
            txtAddress.TabIndex = 3;
            // 
            // txtName
            // 
            txtName.Location = new Point(68, 27);
            txtName.Name = "txtName";
            txtName.Size = new Size(100, 23);
            txtName.TabIndex = 2;
            txtName.TextChanged += textBox1_TextChanged;
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Location = new Point(6, 63);
            label3.Name = "label3";
            label3.Size = new Size(49, 15);
            label3.TabIndex = 1;
            label3.Text = "Address";
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(6, 30);
            label2.Name = "label2";
            label2.Size = new Size(39, 15);
            label2.TabIndex = 0;
            label2.Text = "Name";
            label2.Click += label2_Click;
            // 
            // lstCity
            // 
            lstCity.FormattingEnabled = true;
            lstCity.ItemHeight = 15;
            lstCity.Items.AddRange(new object[] { "Bucharest", "Timisoara", "Oradea" });
            lstCity.Location = new Point(12, 145);
            lstCity.Name = "lstCity";
            lstCity.Size = new Size(120, 94);
            lstCity.TabIndex = 2;
            lstCity.SelectedIndexChanged += lstCity_SelectedIndexChanged;
            // 
            // rdMale
            // 
            rdMale.AutoSize = true;
            rdMale.Location = new Point(269, 38);
            rdMale.Name = "rdMale";
            rdMale.Size = new Size(51, 19);
            rdMale.TabIndex = 3;
            rdMale.TabStop = true;
            rdMale.Text = "Male";
            rdMale.UseVisualStyleBackColor = true;
            // 
            // rdFemale
            // 
            rdFemale.AutoSize = true;
            rdFemale.Location = new Point(269, 76);
            rdFemale.Name = "rdFemale";
            rdFemale.Size = new Size(63, 19);
            rdFemale.TabIndex = 4;
            rdFemale.TabStop = true;
            rdFemale.Text = "Female";
            rdFemale.UseVisualStyleBackColor = true;
            // 
            // chkC
            // 
            chkC.AutoSize = true;
            chkC.Location = new Point(269, 145);
            chkC.Name = "chkC";
            chkC.Size = new Size(41, 19);
            chkC.TabIndex = 5;
            chkC.Text = "C#";
            chkC.UseVisualStyleBackColor = true;
            // 
            // chkASP
            // 
            chkASP.AutoSize = true;
            chkASP.Location = new Point(269, 179);
            chkASP.Name = "chkASP";
            chkASP.Size = new Size(71, 19);
            chkASP.TabIndex = 6;
            chkASP.Text = "ASP.NET";
            chkASP.UseVisualStyleBackColor = true;
            // 
            // btnSubmit
            // 
            btnSubmit.Location = new Point(269, 216);
            btnSubmit.Name = "btnSubmit";
            btnSubmit.Size = new Size(75, 23);
            btnSubmit.TabIndex = 7;
            btnSubmit.Text = "Submit";
            btnSubmit.UseVisualStyleBackColor = true;
            btnSubmit.Click += button1_Click;
            // 
            // treeView1
            // 
            treeView1.Location = new Point(406, 24);
            treeView1.Name = "treeView1";
            treeNode1.Name = "Node1";
            treeNode1.Text = "Label";
            treeNode2.Name = "Node4";
            treeNode2.Text = "Button";
            treeNode3.Name = "Node5";
            treeNode3.Text = "Checkbox";
            treeNode4.Name = "Node0";
            treeNode4.Text = "Root";
            treeView1.Nodes.AddRange(new TreeNode[] { treeNode4 });
            treeView1.Size = new Size(121, 97);
            treeView1.TabIndex = 8;
            treeView1.AfterSelect += treeView1_AfterSelect;
            // 
            // pictureBox1
            // 
            pictureBox1.BackgroundImageLayout = ImageLayout.Center;
            pictureBox1.Image = (Image)resources.GetObject("pictureBox1.Image");
            pictureBox1.InitialImage = (Image)resources.GetObject("pictureBox1.InitialImage");
            pictureBox1.Location = new Point(406, 193);
            pictureBox1.Name = "pictureBox1";
            pictureBox1.Size = new Size(121, 94);
            pictureBox1.TabIndex = 9;
            pictureBox1.TabStop = false;
            // 
            // btnNext
            // 
            btnNext.Location = new Point(269, 264);
            btnNext.Name = "btnNext";
            btnNext.Size = new Size(75, 23);
            btnNext.TabIndex = 10;
            btnNext.Text = "Next";
            btnNext.UseVisualStyleBackColor = true;
            btnNext.Click += btnNext_Click;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            BackgroundImageLayout = ImageLayout.Center;
            ClientSize = new Size(578, 358);
            Controls.Add(btnNext);
            Controls.Add(pictureBox1);
            Controls.Add(treeView1);
            Controls.Add(btnSubmit);
            Controls.Add(chkASP);
            Controls.Add(chkC);
            Controls.Add(rdFemale);
            Controls.Add(rdMale);
            Controls.Add(lstCity);
            Controls.Add(groupBox1);
            Controls.Add(label1);
            Name = "Form1";
            Text = "Aplicatie1";
            Load += Form1_Load;
            groupBox1.ResumeLayout(false);
            groupBox1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)pictureBox1).EndInit();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label label1;
        private GroupBox groupBox1;
        private Label label3;
        private Label label2;
        private TextBox txtAddress;
        private TextBox txtName;
        private ListBox lstCity;
        private RadioButton rdMale;
        private RadioButton rdFemale;
        private CheckBox chkC;
        private CheckBox chkASP;
        private Button btnSubmit;
        private TreeView treeView1;
        private PictureBox pictureBox1;
        private Button btnNext;
    }
}
