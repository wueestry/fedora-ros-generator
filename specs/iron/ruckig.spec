# Meta Package
Name:           ros-iron-ruckig
Version:        0.9.2
Release:        1%{?dist}
License:        MIT
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-ruckig and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-ruckig
Requires:       ros2-iron-ruckig-devel

Obsoletes: ros-iron-ruckig < 0.9.2-1

%description
Instantaneous Motion Generation for Robots and Machines.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.9.2-1
- Update to latest release
