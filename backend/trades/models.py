from django.db import models

class TradeJournal(models.Model):
    TRADE_TYPE = (("BUY", "Buy"), ("SELL", "Sell"))

    # Core trade info
    symbol = models.CharField(max_length=20)
    trade_type = models.CharField(max_length=4, choices=TRADE_TYPE)
    buy_date = models.DateField(null=True, blank=True)
    strategy = models.CharField(max_length=100, null=True, blank=True)

    entry_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    stop_loss = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    target_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    quantity = models.PositiveIntegerField()
    exit_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pyramiding = models.CharField(max_length=50, null=True, blank=True)

    # Calculated financials
    price = models.DecimalField(max_digits=10, decimal_places=2)  # current trade price
    buy_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    broker_commission = models.DecimalField(max_digits=8, decimal_places=2)
    sebon_fee = models.DecimalField(max_digits=8, decimal_places=2)
    dp_charge = models.DecimalField(max_digits=8, decimal_places=2)
    capital_gain_tax = models.DecimalField(max_digits=8, decimal_places=2)

    gross_amount = models.DecimalField(max_digits=12, decimal_places=2)
    net_amount = models.DecimalField(max_digits=12, decimal_places=2)

    # Journal fields from Excel
    profit_loss_rs = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    profit_loss_percent = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    emotions_entry = models.TextField(null=True, blank=True)
    emotions_exit_profit = models.TextField(null=True, blank=True)
    emotions_exit_sl = models.TextField(null=True, blank=True)

    learning = models.TextField(null=True, blank=True)
    mistakes = models.TextField(null=True, blank=True)

    rating_execution = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    chart_link = models.URLField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.symbol} ({self.trade_type})"