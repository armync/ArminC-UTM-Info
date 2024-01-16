namespace Aplicatie2
{
    partial class Calculator
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
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
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            cbOperator = new ComboBox();
            txtOp1 = new TextBox();
            txtOp2 = new TextBox();
            btnCalculeaza = new Button();
            txtRezultat = new TextBox();
            lbEqual = new Label();
            lblCalcul = new Label();
            btnBack = new Button();
            btnReset = new Button();
            SuspendLayout();
            // 
            // cbOperator
            // 
            cbOperator.BackColor = SystemColors.MenuBar;
            cbOperator.FormattingEnabled = true;
            cbOperator.Items.AddRange(new object[] { "+", "-", "*", "/", "^" });
            cbOperator.Location = new Point(102, 73);
            cbOperator.Name = "cbOperator";
            cbOperator.Size = new Size(58, 23);
            cbOperator.TabIndex = 0;
            // 
            // txtOp1
            // 
            txtOp1.Location = new Point(24, 73);
            txtOp1.Name = "txtOp1";
            txtOp1.Size = new Size(72, 23);
            txtOp1.TabIndex = 1;
            // 
            // txtOp2
            // 
            txtOp2.BackColor = SystemColors.Window;
            txtOp2.Location = new Point(166, 73);
            txtOp2.Name = "txtOp2";
            txtOp2.Size = new Size(72, 23);
            txtOp2.TabIndex = 2;
            // 
            // btnCalculeaza
            // 
            btnCalculeaza.Location = new Point(65, 166);
            btnCalculeaza.Name = "btnCalculeaza";
            btnCalculeaza.Size = new Size(95, 26);
            btnCalculeaza.TabIndex = 3;
            btnCalculeaza.Text = "Calculeaza";
            btnCalculeaza.UseVisualStyleBackColor = true;
            // 
            // txtRezultat
            // 
            txtRezultat.BackColor = SystemColors.ButtonFace;
            txtRezultat.BorderStyle = BorderStyle.None;
            txtRezultat.Location = new Point(267, 77);
            txtRezultat.Name = "txtRezultat";
            txtRezultat.Size = new Size(98, 16);
            txtRezultat.TabIndex = 4;
            // 
            // lbEqual
            // 
            lbEqual.AutoSize = true;
            lbEqual.Location = new Point(244, 77);
            lbEqual.Name = "lbEqual";
            lbEqual.Size = new Size(15, 15);
            lbEqual.TabIndex = 5;
            lbEqual.Text = "=";
            // 
            // lblCalcul
            // 
            lblCalcul.AutoSize = true;
            lblCalcul.Location = new Point(24, 40);
            lblCalcul.Name = "lblCalcul";
            lblCalcul.Size = new Size(93, 15);
            lblCalcul.TabIndex = 6;
            lblCalcul.Text = "Introdu calculul:";
            // 
            // btnBack
            // 
            btnBack.Location = new Point(166, 167);
            btnBack.Name = "btnBack";
            btnBack.Size = new Size(32, 26);
            btnBack.TabIndex = 7;
            btnBack.Text = "M";
            btnBack.UseVisualStyleBackColor = true;
            btnBack.Click += btnBack_Click;
            // 
            // btnReset
            // 
            btnReset.Location = new Point(204, 169);
            btnReset.Name = "btnReset";
            btnReset.Size = new Size(75, 23);
            btnReset.TabIndex = 9;
            btnReset.Text = "Reset";
            btnReset.UseVisualStyleBackColor = true;
            btnReset.Click += btnReset_Click;
            // 
            // Calculator
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(377, 215);
            Controls.Add(btnReset);
            Controls.Add(btnBack);
            Controls.Add(lblCalcul);
            Controls.Add(lbEqual);
            Controls.Add(txtRezultat);
            Controls.Add(btnCalculeaza);
            Controls.Add(txtOp2);
            Controls.Add(txtOp1);
            Controls.Add(cbOperator);
            Name = "Calculator";
            Text = "Calculator";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private ComboBox cbOperator;
        private TextBox txtOp1;
        private TextBox txtOp2;
        private Button btnCalculeaza;
        private TextBox txtRezultat;
        private Label lbEqual;
        private Label lblCalcul;
        private Button btnBack;
        private Button button1;
        private Button btnReset;
    }
}