o
    ���b*<  �                   @   sx  d dl mZmZ d dlZd dlmZ d dlmZmZm	Z	m
Z
mZmZmZ d dlmZ d dlmZmZ d dlmZ d dlmZmZmZ d d	lmZ d d
l mZ d dlmZ d dlmZmZ d dlZd dlZd dlZd dl Z d dl!Z!d dl"Z"e�  d dl#T ej$Z%ej&Z'ej(Z)ej*Z+ej,Z-ej.Z/ej0Z1ej2Z3ej4Z)ej5Z'ej$Z6ej*Z+dZ7ej,Z-ej8Z/e)e'e+e/e-gZ9e'd e+ d e' d e6 Z:e'd e) d e' d e6 Z;e+d e' d e+ d e6 Z<e'd e- d e' d e6 Z=e+d e' d e+ d e6 Z>e+d e' d e+ d e6 Z?e'e)e+e-e/e3e1gZ9dd� Z@dZAdZBdd� ZCdd� ZDdd � ZEd!d"� ZFd#d$� ZGd%d&� ZHd'd(� ZId)d*� ZJd+d,� ZKeK�  dS )-�    )�Client�filtersN)�ImportChatInvite)�	FloodWait�ApiIdInvalid�PhoneCodeExpired�PhoneCodeInvalid�UserNotParticipant�PhoneNumberInvalid�SessionPasswordNeeded)�PhoneNumberBanned)�
BadRequest�	Forbidden)�UserPrivacyRestricted)�PeerIdInvalid�ChatAdminRequired�	PeerFlood)�lol_py)�errors)r   )�init�Fore)�*z[97m�[�i�]�!r   �~�+�-c                  C   s,   dd l } t�d� | jddd�}t|� d S )Nr   �clear�   Beast�slant�Zfont)�pyfiglet�os�system�figlet_formatr   )r#   �result� r(   �#/storage/emulated/0/protonic/dec.py�banner>   s   
r*   i<|z Z 9b70b20efd67e9b99edc395d78407cfac                  C   s"  t �d� g } tdd���y}ttdt� dt� ���}t|�D �]^}ttdt� dt� ���}d�	|�
� �}t�|g|� | �|� tdt� d�� | D �]1}td	|� �ttd
�}|�� }|�scz|�|�}	W n9 ty� }
 ztt� |
� t� �� W Y d }
~
n"d }
~
w ty�   td� Y n ty�   tt� dt� �� Y nw ztt� dt� ��}W n ty�   tt� d�� Y nw |}z|j||	jd�	t|��d� W n� ty�   tt� d�� Y n} ty�   tt� d�� Y nn t�y:   z	tt� d��}W n; t�y7   tt� d�� |}z|�|� W n  t�y4 }
 ztt� dt� t|
�� �� W Y d }
~
nd }
~
ww Y nw Y n  t�yY }
 ztt� dt � t|
�� �� W Y d }
~
nd }
~
ww td� |�!�  qJ|�r|tt� |�"� j#� dt$� dt� d�� |�!�  qJqW d   � d S 1 �s�w   Y  d S )Nr   �vars.txt�ab�
z& [~] Enter number of accounts to add: z [~] Enter Phone Number: � z# [i] Saved all accounts in vars.txt�memory/��api_id�api_hashzsed api invalidz%The Provided Phone Number is invalid.zenter otp ypu recivedzTimeout.� )Z
phone_codezInvalid OtpzThe otp has been expiredzSend 2FA Passwordz* Sorry You have reached limit of 5 Minuteszerror :z[+] login Successfulz: z----> Signed Up Sucess

)%r$   r%   �open�int�input�lg�r�range�str�join�split�pickle�dump�append�printr   r1   r2   �connect�	send_coder   r   r
   �TimeoutErrorZsign_inZphone_code_hashr   r   r   �mgZcheck_password�	Exception�ye�
disconnect�get_me�
first_name�cy)Znew_accs�gZnumber_to_addr   Zphone_numberZparsed_numberZnumber�session�
authorized�code�eZotpZotp_codeZtwo_step_codeZnew_coder(   r(   r)   �loginM   s�   


 ��� &�����&��
$���$�rP   c               	   C   s�  t �d� t�  td� g } g }tdd�}	 z
| �t�|�� W n	 ty)   Y nw q|�	�  t
| �dkrAttd � td� d S | D ]>}t|d �}td	|� �ttd
�}|�� }|s�z|�|� td|� d�� W qC ty�   tt|�d � |�|� Y qCw qCt
|�dkr�td� td� d S |D ]8}| �|� tdd��}| D ]}	|	d }
t�|
g|� q�W d   � n1 s�w   Y  |�	�  td� td� q�d S )Nr   z;This Process Maybe Take some time depending on your accountr+   �rbTr   z4[!] There are no accounts! Please add some and retry�   r/   r0   z[+] z is not bannedz is banned!zCongrats! No banned accounts�!
Press enter to goto main menu...�wbz[i] All banned accounts removed)r$   r%   r*   r@   r4   r?   r=   �load�EOFError�close�lenr8   �sleepr:   r   r1   r2   rA   rB   r   r6   �remover>   )�accountsZbanned_accs�h�account�phonerL   rM   �m�k�aZPhoner(   r(   r)   �banfltr�   sZ   

��
��
��
�rb   c                  C   s  t �d� g } tdd�}	 z
| �t�|�� W n	 ty    Y nw q|��  d}td� | D ]}td|� d|d � �� |d	7 }q.t	t
d
t� ���}t| | d �}|d }t jdkrdt �d|� �� nt �d|� �� | |= tdd�}| D ]}t�||� qvtd� t
d� |��  d S )Nr   r+   rQ   Tr   z [i] Choose an account to delete
r   z] �   z
[+] Enter a choice: z.session�ntzdel memory\z
rm memory/rT   z
[+] Account DeletedrS   )r$   r%   r4   r?   r=   rU   rV   rW   r@   r5   r6   �nr:   �namer>   )�accs�fr   �acc�indexr^   Zsession_filer]   r(   r(   r)   �remacc�   s:   

��


rk   c                  C   s�   t �d� g } tdd�}	 z
| �t�|�� W n	 ty    Y nw q|��  td� td� d}| D ]}td|d � �� |d	7 }q2td� t	d
� d S )Nr   r+   rQ   Tz	List Of Phone Numbers Arez ================================r   �	rc   z
Press enter to goto main menu)
r$   r%   r4   r?   r=   rU   rV   rW   r@   r6   )rg   rh   r   �zr(   r(   r)   �display�   s&   

��
rn   c            $         s�	  dd� � g } t dd�}	 z
| �t�|�� W n	 ty   Y nw qtdt� d�� | D ]m}|d }tt� t� d	t� |� �� t	d
|� �t
td�}|�� }g }|s{z|�|� td� W n tyz   tt� dt� |� dt� dt� �� |�|� Y nw |D ]}| �|� ttt d t � q}t�d� |��  q+ttd � � �  t�  dd� }� fdd�}	z`t dd��}t�|�}
|��  W d   � n1 s�w   Y  tt� t� dt� |
d � t� dt� ��}d|v r�|
d }t|
d �}ntjdkr�t� d� nt� d� tt� t� dt� ��}d}W n   tt� t� dt� ��}d}Y g } t dd�}	 z
| �t�|�� W n
 t�y=   Y nw �q)tt� t� dt� t!| �� �� ttt� t� d t� ���}tt� t� d!t� �� tt� d"t� d#�� tt� d$t� d%�� ttt� t� d&t� ���}|dk�r�t"tt� t� d't� ���}nt"tt� t� d(t� ���}tt� d)�d* � d+d,� | d |� D �}|D ]}| �|� �q�t dd-��$}| D ]	}t�#||� �q�|D ]	}t�#||� �q�|��  W d   � n	1 �s�w   Y  ttt� t� d.t� d/t� d0t� d1t� �
��}tt$� t� d2t� t!|�� t� d3�� d}d}|D �]�}|d4 }t	d
|d � �t
td�}tt� t� d5t� |d � t� d6t� d7�	� |��  |�%� j&}z�d8|v �r�|�'d8�d }z|t(|�� tt� t� d5t� |� t� d9�� W n   Y n|�)|� tt� t� d5t� |� t� d9�� |dk�r�|�)|� tt� t� d5t� |� t� d:�� n$z|�'d8�d }|t(|�� tt� t� d5t� |� t� d:�� W n   Y W n/ t*�y } z"tt� t� d5t� |� t� d;�� tt� dt� |� �� W Y d }~�q'd }~ww tt� t� d5t� |� t� d6t� d<�	� z	g }|�+|�}W n( t*�yL } ztt� t� d=�� tt� t� d|� �� W Y d }~�q'd }~ww t!t"|��}|dk�sZJ �||k�rjtt� t� d>�� �q'tt� t� d?t� |� �� d}d}|D �]F}|d7 }|d@k�r�tt� t� dA��  �n0z0|dk�r�|�,||j-j.� n|�,||j-j.� tdBt/� |j-j&� t� dC�� |d7 }t�|� W �q} t0�y� }  z|d7 }tt� dD�� W Y d } ~ �q}d } ~ w t1�y   tt2� t� d5t� |j-j&� t� d6t� dE�	� Y �q} t3�y, }! ztt2� t� d5t� |j-j&� t� d6t� |!� �	� W Y d }!~!�q}d }!~!w t4�yU }" ztt2� t� d5t� |j-j&� t� d6t� |"� �	� W Y d }"~"�q}d }"~"w t5�ys }# ztt� t� d|#� �� W Y d }#~# nVd }#~#w t6�y�   tt� t� dF�� Y �q} t7�y�   tt� t� dG�� |t!|�k �r�|||� |	�  Y �q} t*�y� } ztt� d|� �� W Y d }~�q}d }~ww |��  �q'|dk�r�tdHt� t� dI�� z||k �r�|||� |	�  W d S    |	�  Y d S )JNc                   S   s&   t jdkrt �d� d S t �d� d S )Nrd   �clsr   )r$   rf   r%   r(   r(   r(   r)   �clr�   s   
zmrunal.<locals>.clrr+   rQ   Tz
 zChecking for banned accounts...r   z
 Checking r/   r0   zThis Phone Is Logged outr3   z
is banned!z Banned account removedg      �?z Sessions created!c                 S   s`   t dd��}t�| t|�g|� |��  W d   � n1 sw   Y  tt� t� dt� �� d S )N�
status.datrT   z Session stored )r4   r=   r>   r5   rW   r@   �infor7   )Zscrapedrj   rh   r(   r(   r)   �
log_status  s
   
�zmrunal.<locals>.log_statusc                      s(   t dt� d�� � �  t�  t��  d S )Nr-   z Press enter to exit...)r6   rJ   r*   �sys�exitr(   �rp   r(   r)   �exit_window  s   zmrunal.<locals>.exit_windowrq   z Resume scraping members from z	? [y/n]: �yrc   rd   zdel status.datzrm status.datz. Public/Private group link to scrape members: z Total accounts In Memory: z" Enter number of accounts to use: z Choose an optionz[0]z Add to public groupz[1]z Add to private groupz Enter choice: z Enter public group link: z Enter private group link: �_�2   c                 S   s   g | ]}|�qS r(   r(   )�.0�xr(   r(   r)   �
<listcomp>?  s    zmrunal.<locals>.<listcomp>rT   z Enter delay time per requestr   z
0 for Nonez]: z -- Adding members from z account(s) --�<   z User: z -- zStarting session... z
/joinchat/z -- Joined group to scrapez -- Joined group to addz -- Failed to join groupzRetrieving entities...z Couldn't scrape membersz No members to add!z Start: �
   z/ Too many Peer Flood Errors! Closing session...z==>z-->DONEz Peer Flood Error z User Privacy Errorz Error in Given Valuez ---- Adding Terminated ----r-   z session ended)8r4   r?   r=   rU   rV   r@   r7   �plus�greyr   r1   r2   rA   rB   r   �error�wr8   �rsrZ   rr   �timerY   rG   r*   rW   r6   �INPUTrJ   r5   r$   rf   r%   rX   r:   r>   �successrH   rI   r<   r   Z	join_chatrE   Zget_chat_membersZadd_chat_members�user�idrD   r   r   �minusr   r   r   �
ValueError�KeyboardInterrupt)$r[   rh   ra   ZphnrL   rM   Zbannedrm   rs   rw   �statusZlolZscraped_grprj   Znumber_of_accs�choice�targetZto_use�lr,   Z
sleep_timeZadding_statusZapprox_members_countri   �stopZacc_nameZg_hashZgrp_hashrO   �membersZpeer_flood_statusr�   Zpf�o�pp�opr(   rv   r)   �mrunal�   sv  
��
"�




�(

�
��

�,$
*

$
 

"$� ��&��



�0,�,��
��


r�   c                  C   s  t �d� tjddd�} d| � d�}t|� ttd��}|dkr%t�  d S |d	kr.t�  d S |d
kr7t	�  d S |dkr@t
�  d S |dkrIt�  d S |dkr_dd l}t�d	� |�g d�� d S |dkrudd l}t�d	� |�g d�� d S |dkrtd� d S d S )Nr   r    r!   r"   r-   a4  
!~/~/~/~/~Telegram:-@BeastX_Bots ~/~/~/~/~!
!~/~/~/~/~ Dev:- @GodmrunaL ~/~/~/~/~!

Select Option:

       [1] Add new accounts
       [2] Ban Filter
       [3] Remove specific accounts
       [4] Members Adding
       [5] Display All Accounts
       [6] Watch Toturial
       [7] Need Help
       [8] Quit
zEnter Choice:  rc   �   rR   �   �   �   r   )�am�startz4https://youtube.com/channel/UCB3efA4MKr-JkBcEJPdYqBg�   )r�   r�   zhttps://t.me/BeastX_Support�   ZDone)r$   r%   r#   r&   r   r5   r6   rP   rb   rk   r�   rn   �
subprocessr�   rY   Zcheck_outputr@   )r'   �textra   r�   r(   r(   r)   �main�  s8   
�






�r�   c                  C   sF   d} t d�D ]}t�d� tj�d| |t| �   � tj��  qd S )Nz|/-\�(   g�������?zCheacking For Updates....)r9   r�   rY   rt   �stdout�writerX   �flush)ZO0OOOOOO000000OOOZO0O00OOOOOOOOO0OOr(   r(   r)   �starting_bot�  s   
�r�   c               
   C   s(  t �  t�d� zt�d�} W n   td� Y zdt| j�tkr7tt	� d�� t
�d� t�d� t�  W d S ttj� d| j� d�� ttj� d�� tjd	kr[t�d
� t�d� n
t�d� t�d� t�d� t�d� ttj� d| j� �� W d S  ty� } zt|� W Y d }~d S d }~ww )Nr   z?https://raw.githubusercontent.com/msy1717/vers/main/version.txtzcheck internetz#[+]Your Beast Script Is Up to date r�   z[~]Update available[Version:z].z[i] Downloading updates...rd   zdel beast.pyzdel version.pyzrm beast.pyzrm version.pyzGcurl -l -O https://raw.githubusercontent.com/msy1717/vers/main/beast.pyzIcurl -l -O https://raw.githubusercontent.com/msy1717/vers/main/version.pyz[*] Updated to version: )r�   r$   r%   �requests�getr@   �floatr�   �versionrJ   r�   rY   r�   r   �GREENrf   rE   )ZsedrO   r(   r(   r)   �update�  s4   









��r�   c                  C   s�   z7d} t �| �}|jdkrt�  |jdkr5t�  tdt� dt� dt� dt� dt� dt� dt� d	�� W d S W d S  t	yN } zt|� W Y d }~d S d }~ww )
Nz!https://pastebin.com/raw/G57VFCtmZonZoffzN
            
            
            
            
            
            r   �%r   zServer Offlinez]]
            
            
            
            
            
            
            
)
r�   r�   r�   r�   r*   r@   r7   re   rJ   rE   )Zurls1ZswitchsrK   r(   r(   r)   �onoff  s6   


����������r�   )LZpyrogramr   r   r=   Zpyrogram.raw.functions.messagesr   Zpyrogram.errorsr   r   r   r   r	   r
   r   Z*pyrogram.errors.exceptions.bad_request_400r   r   r   Z(pyrogram.errors.exceptions.forbidden_403r   r   r   r   Z	lolpythonr   r   Zcoloramar   r   r�   rt   r�   r$   r�   r#   r�   ZRESETre   ZLIGHTGREEN_EXr7   ZLIGHTRED_EXr8   ZWHITEr�   ZCYANrJ   ZLIGHTYELLOW_EXrF   ZLIGHTMAGENTA_EXrD   ZLIGHTBLUE_EXZlbZREDr�   r�   r�   ZYELLOWZcolorsrr   r�   r�   r�   r�   r�   r*   r1   r2   rP   rb   rk   rn   r�   r�   r�   r�   r�   r(   r(   r(   r)   �<module>   sr   $>, I, 
