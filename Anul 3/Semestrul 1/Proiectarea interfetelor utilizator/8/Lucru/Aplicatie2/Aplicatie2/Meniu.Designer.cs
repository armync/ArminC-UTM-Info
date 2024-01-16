namespace Aplicatie2
{
    partial class Meniu
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
            btnCalculator = new Button();
            btnConversie = new Button();
            btn3 = new Button();
            btn4 = new Button();
            btnQuestion = new Button();
            SuspendLayout();
            // 
            // btnCalculator
            // 
            btnCalculator.Location = new Point(135, 83);
            btnCalculator.Name = "btnCalculator";
            btnCalculator.Size = new Size(75, 23);
            btnCalculator.TabIndex = 0;
            btnCalculator.Text = "Caculator";
            btnCalculator.UseVisualStyleBackColor = true;
            btnCalculator.Click += btnCalculator_Click;
            // 
            // btnConversie
            // 
            btnConversie.Location = new Point(135, 125);
            btnConversie.Name = "btnConversie";
            btnConversie.Size = new Size(75, 23);
            btnConversie.TabIndex = 1;
            btnConversie.Text = "Conversie";
            btnConversie.UseVisualStyleBackColor = true;
            btnConversie.Click += btnConversie_Click;
            // 
            // btn3
            // 
            btn3.BackColor = SystemColors.Desktop;
            btn3.Location = new Point(135, 211);
            btn3.Name = "btn3";
            btn3.Size = new Size(75, 23);
            btn3.TabIndex = 2;
            btn3.Text = "3";
            btn3.UseVisualStyleBackColor = false;
            btn3.Click += btn3_Click;
            // 
            // btn4
            // 
            btn4.BackColor = SystemColors.HotTrack;
            btn4.ForeColor = SystemColors.ControlText;
            btn4.Location = new Point(135, 283);
            btn4.Name = "btn4";
            btn4.Size = new Size(75, 23);
            btn4.TabIndex = 3;
            btn4.Text = "4";
            btn4.UseVisualStyleBackColor = false;
            btn4.Click += btn4_Click;
            // 
            // btnQuestion
            // 
            btnQuestion.Location = new Point(216, 211);
            btnQuestion.Name = "btnQuestion";
            btnQuestion.Size = new Size(33, 23);
            btnQuestion.TabIndex = 4;
            btnQuestion.Text = "?";
            btnQuestion.UseVisualStyleBackColor = true;
            // 
            // Meniu
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(353, 371);
            Controls.Add(btnQuestion);
            Controls.Add(btn4);
            Controls.Add(btn3);
            Controls.Add(btnConversie);
            Controls.Add(btnCalculator);
            Name = "Meniu";
            Text = "Aplicatie2";
            ResumeLayout(false);
        }

        #endregion

        private Button btnCalculator;
        private Button btnConversie;
        private Button btn3;
        private Button btn4;
        private Button btnQuestion;
    }
}
