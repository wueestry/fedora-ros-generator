# Meta Package
Name:           ros-jazzy-keyboard-handler
Version:        0.3.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-keyboard_handler and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-keyboard_handler
Requires:       ros2-jazzy-keyboard_handler-devel

Obsoletes: ros-jazzy-keyboard-handler < 0.3.1-1

%description
Handler for input from keyboard

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.3.1-1
- Update to latest release
