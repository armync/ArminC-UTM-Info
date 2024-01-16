namespace Aplicatie2
{
    partial class Conversie
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
            cbConvert = new ComboBox();
            txt1 = new TextBox();
            txt2 = new TextBox();
            btnConversie = new Button();
            btnReset = new Button();
            lblLine = new Label();
            lblTxtConversie = new Label();
            btnMeniu = new Button();
            SuspendLayout();
            // 
            // cbConvert
            // 
            cbConvert.BackColor = SystemColors.Menu;
            cbConvert.FormattingEnabled = true;
            cbConvert.Items.AddRange(new object[] { "Inch -> CM", "Celsius -> Fahrenheit", "Mile -> KM", "Meter -> Yard", "Liters -> M3" });
            cbConvert.Location = new Point(137, 85);
            cbConvert.Name = "cbConvert";
            cbConvert.Size = new Size(142, 23);
            cbConvert.TabIndex = 0;
            // 
            // txt1
            // 
            txt1.Location = new Point(24, 127);
            txt1.Name = "txt1";
            txt1.Size = new Size(100, 23);
            txt1.TabIndex = 1;
            // 
            // txt2
            // 
            txt2.Location = new Point(294, 127);
            txt2.Name = "txt2";
            txt2.Size = new Size(100, 23);
            txt2.TabIndex = 2;
            // 
            // btnConversie
            // 
            btnConversie.Location = new Point(100, 194);
            btnConversie.Name = "btnConversie";
            btnConversie.Size = new Size(88, 23);
            btnConversie.TabIndex = 3;
            btnConversie.Text = "Converteste";
            btnConversie.UseVisualStyleBackColor = true;
            btnConversie.Click += btnConversie_Click;
            // 
            // btnReset
            // 
            btnReset.Location = new Point(225, 194);
            btnReset.Name = "btnReset";
            btnReset.Size = new Size(88, 23);
            btnReset.TabIndex = 4;
            btnReset.Text = "Reseteaza";
            btnReset.UseVisualStyleBackColor = true;
            btnReset.Click += btnReset_Click;
            // 
            // lblLine
            // 
            lblLine.AutoSize = true;
            lblLine.Location = new Point(174, 130);
            lblLine.Name = "lblLine";
            lblLine.Size = new Size(59, 15);
            lblLine.TabIndex = 5;
            lblLine.Text = "<            >";
            // 
            // lblTxtConversie
            // 
            lblTxtConversie.AutoSize = true;
            lblTxtConversie.Location = new Point(22, 35);
            lblTxtConversie.Name = "lblTxtConversie";
            lblTxtConversie.Size = new Size(102, 15);
            lblTxtConversie.TabIndex = 6;
            lblTxtConversie.Text = "Introdu conversia:";
            // 
            // btnMeniu
            // 
            btnMeniu.Location = new Point(194, 194);
            btnMeniu.Name = "btnMeniu";
            btnMeniu.Size = new Size(25, 23);
            btnMeniu.TabIndex = 7;
            btnMeniu.Text = "M";
            btnMeniu.UseVisualStyleBackColor = true;
            btnMeniu.Click += btnMeniu_Click;
            // 
            // Conversie
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(429, 244);
            Controls.Add(btnMeniu);
            Controls.Add(lblTxtConversie);
            Controls.Add(lblLine);
            Controls.Add(btnReset);
            Controls.Add(btnConversie);
            Controls.Add(txt2);
            Controls.Add(txt1);
            Controls.Add(cbConvert);
            Name = "Conversie";
            Text = "Conversie";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private ComboBox cbConvert;
        private TextBox txt1;
        private TextBox txt2;
        private Button btnConversie;
        private Button btnReset;
        private Label lblLine;
        private Label lblTxtConversie;
        private Button btnMeniu;
    }
}