"""
Email Service Module
Handles email sending using SendGrid for reservations and contact forms
"""
from typing import Optional
import os
import ssl
import urllib3
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from app.core.config import settings

# Disable SSL warnings and set unverified context (for environments with SSL issues)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context


class EmailService:
    """Service for sending transactional emails via SendGrid"""
    
    def __init__(self):
        self.api_key = settings.sendgrid_api_key
        self.from_email = settings.sendgrid_from_email
        self.from_name = settings.sendgrid_from_name
        self.restaurant_email = settings.restaurant_notification_email
        
        if self.api_key and self.api_key != "":
            print("✅ SendGrid email service initialized")
            print(f"   From: {self.from_email}")
        else:
            print("⚠️  SendGrid API key not configured")
    
    def send_reservation_confirmation(
        self, 
        to_email: str, 
        name: str, 
        date: str, 
        time: str, 
        party_size: int,
        reservation_id: str,
        special_requests: Optional[str] = None
    ) -> bool:
        """Send reservation confirmation email to customer"""
        
        if not self.api_key:
            print("⚠️  Email service not configured")
            return False
        
        # Format special requests section
        special_requests_html = ""
        if special_requests:
            special_requests_html = f"""
            <div style="margin-top: 15px; padding-top: 15px; border-top: 2px dashed #e0e0e0;">
                <p style="margin: 0; font-weight: 600; color: #667eea; margin-bottom: 8px;">📝 Special Requests:</p>
                <p style="margin: 0; color: #555; line-height: 1.6;">{special_requests}</p>
            </div>
            """
        
        # HTML email template
        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
        </head>
        <body style="margin: 0; padding: 0; font-family: Arial, sans-serif; background-color: #f5f5f5;">
            <table role="presentation" style="width: 100%; border-collapse: collapse;">
                <tr>
                    <td style="padding: 40px 20px;">
                        <table role="presentation" style="max-width: 600px; margin: 0 auto; background-color: #ffffff; border-radius: 16px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.1);">
                            <tr>
                                <td style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 40px 30px; text-align: center;">
                                    <h1 style="margin: 0; color: #ffffff; font-size: 32px; font-weight: 700;">🎉 Reservation Confirmed!</h1>
                                    <p style="margin: 10px 0 0 0; color: rgba(255,255,255,0.95); font-size: 16px;">We're excited to serve you!</p>
                                </td>
                            </tr>
                            <tr>
                                <td style="padding: 40px 30px;">
                                    <p style="margin: 0 0 20px 0; font-size: 18px; color: #333; font-weight: 600;">Hello {name},</p>
                                    <p style="margin: 0 0 30px 0; font-size: 15px; color: #555; line-height: 1.6;">
                                        Thank you for choosing <strong style="color: #667eea;">{settings.restaurant_name}</strong>! 
                                        Your reservation has been confirmed.
                                    </p>
                                    <div style="background: linear-gradient(135deg, #f8f9ff 0%, #f3f4ff 100%); padding: 25px; border-radius: 12px; border-left: 5px solid #667eea; margin-bottom: 30px;">
                                        <h2 style="margin: 0 0 20px 0; color: #667eea; font-size: 20px; font-weight: 700;">📅 Reservation Details</h2>
                                        <table style="width: 100%; border-collapse: collapse;">
                                            <tr>
                                                <td style="padding: 10px 0; border-bottom: 1px solid rgba(102, 126, 234, 0.1);"><span style="color: #666; font-size: 14px;">📆 Date</span></td>
                                                <td style="padding: 10px 0; border-bottom: 1px solid rgba(102, 126, 234, 0.1); text-align: right;"><strong style="color: #333; font-size: 15px;">{date}</strong></td>
                                            </tr>
                                            <tr>
                                                <td style="padding: 10px 0; border-bottom: 1px solid rgba(102, 126, 234, 0.1);"><span style="color: #666; font-size: 14px;">⏰ Time</span></td>
                                                <td style="padding: 10px 0; border-bottom: 1px solid rgba(102, 126, 234, 0.1); text-align: right;"><strong style="color: #333; font-size: 15px;">{time}</strong></td>
                                            </tr>
                                            <tr>
                                                <td style="padding: 10px 0; border-bottom: 1px solid rgba(102, 126, 234, 0.1);"><span style="color: #666; font-size: 14px;">👥 Party Size</span></td>
                                                <td style="padding: 10px 0; border-bottom: 1px solid rgba(102, 126, 234, 0.1); text-align: right;"><strong style="color: #333; font-size: 15px;">{party_size} guest{"s" if party_size > 1 else ""}</strong></td>
                                            </tr>
                                            <tr>
                                                <td style="padding: 10px 0;"><span style="color: #666; font-size: 14px;">🎫 Confirmation #</span></td>
                                                <td style="padding: 10px 0; text-align: right;"><code style="background: #ffffff; padding: 6px 12px; border-radius: 6px; color: #667eea; font-size: 14px; font-weight: 600; border: 1px solid #667eea;">{reservation_id}</code></td>
                                            </tr>
                                        </table>
                                        {special_requests_html}
                                    </div>
                                    <div style="background: #fff9e6; padding: 20px; border-radius: 8px; border-left: 4px solid #ffc107; margin-bottom: 25px;">
                                        <p style="margin: 0; color: #856404; font-size: 14px; line-height: 1.6;"><strong>⏱️ Please arrive 10-15 minutes early</strong></p>
                                    </div>
                                    <div style="background: #f9f9f9; padding: 20px; border-radius: 8px; margin-bottom: 25px;">
                                        <h3 style="margin: 0 0 12px 0; color: #333; font-size: 16px; font-weight: 600;">📍 Location & Contact</h3>
                                        <p style="margin: 0; color: #555; font-size: 14px; line-height: 1.6;">
                                            <strong>{settings.restaurant_name}</strong><br>
                                            {settings.restaurant_address}<br>
                                            📞 {settings.restaurant_phone}
                                        </p>
                                    </div>
                                    <p style="margin: 0; font-size: 15px; color: #555; line-height: 1.6; text-align: center;">We look forward to serving you! 🍽️</p>
                                </td>
                            </tr>
                            <tr>
                                <td style="background: #f9f9f9; padding: 25px 30px; text-align: center; border-top: 1px solid #e0e0e0;">
                                    <p style="margin: 0; color: #999; font-size: 12px;">{settings.restaurant_name} © {date.split('-')[0]}</p>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>
        </body>
        </html>
        """
        
        try:
            message = Mail(
                from_email=self.from_email,
                to_emails=to_email,
                subject=f"✅ Reservation Confirmed - {date} at {time}",
                html_content=html_content
            )
            
            sg = SendGridAPIClient(self.api_key)
            response = sg.send(message)
            
            print(f"✅ Email sent to {to_email} - Status: {response.status_code}")
            return True
            
        except Exception as e:
            print(f"❌ Failed to send email: {str(e)}")
            return False
    
    def send_contact_form_notification(
        self, 
        customer_name: str,
        customer_email: str,
        customer_phone: str,
        message_text: str
    ) -> bool:
        """Send contact form notification to restaurant"""
        
        if not self.api_key:
            print("⚠️  Email service not configured")
            return False
        
        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0;">
        </head>
        <body style="margin: 0; padding: 0; font-family: Arial, sans-serif; background-color: #f5f5f5;">
            <table role="presentation" style="width: 100%; border-collapse: collapse;">
                <tr>
                    <td style="padding: 40px 20px;">
                        <table role="presentation" style="max-width: 600px; margin: 0 auto; background-color: #ffffff; border-radius: 16px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.1);">
                            <tr>
                                <td style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 30px; text-align: center;">
                                    <h1 style="margin: 0; color: #ffffff; font-size: 28px; font-weight: 700;">📧 New Contact Form</h1>
                                    <p style="margin: 10px 0 0 0; color: rgba(255,255,255,0.95); font-size: 15px;">Someone reached out via your website</p>
                                </td>
                            </tr>
                            <tr>
                                <td style="padding: 40px 30px;">
                                    <div style="background: #f8f9ff; padding: 25px; border-radius: 12px; border-left: 5px solid #667eea; margin-bottom: 25px;">
                                        <h2 style="margin: 0 0 20px 0; color: #667eea; font-size: 18px; font-weight: 700;">👤 Customer Information</h2>
                                        <p style="margin: 0 0 10px 0;"><strong>Name:</strong> {customer_name}</p>
                                        <p style="margin: 0 0 10px 0;"><strong>Email:</strong> <a href="mailto:{customer_email}" style="color: #667eea;">{customer_email}</a></p>
                                        <p style="margin: 0;"><strong>Phone:</strong> {customer_phone}</p>
                                    </div>
                                    <div style="background: #f9f9f9; padding: 20px; border-radius: 8px; margin-bottom: 20px;">
                                        <h3 style="margin: 0 0 15px 0; color: #333; font-size: 16px;">💬 Message</h3>
                                        <p style="margin: 0; color: #555; line-height: 1.6; white-space: pre-wrap;">{message_text}</p>
                                    </div>
                                    <div style="background: #e8f5e9; padding: 15px; border-radius: 8px; text-align: center;">
                                        <p style="margin: 0; color: #2e7d32; font-size: 14px;">💡 Reply to this email to respond directly to the customer</p>
                                    </div>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>
        </body>
        </html>
        """
        
        try:
            message = Mail(
                from_email=self.from_email,
                to_emails=self.restaurant_email,
                subject=f"📧 Contact Form: {customer_name}",
                html_content=html_content
            )
            message.reply_to = customer_email
            
            sg = SendGridAPIClient(self.api_key)
            response = sg.send(message)
            
            print(f"✅ Contact notification sent to {self.restaurant_email} - Status: {response.status_code}")
            return True
            
        except Exception as e:
            print(f"❌ Failed to send contact notification: {str(e)}")
            return False


# Singleton instance
email_service = EmailService()
