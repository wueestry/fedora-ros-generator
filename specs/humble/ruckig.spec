# Meta Package
Name:           ros-humble-ruckig
Version:        0.9.2
Release:        1%{?dist}
License:        MIT
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-ruckig and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-ruckig
Requires:       ros2-humble-ruckig-devel

Obsoletes: ros-humble-ruckig < 0.9.2-1

%description
Instantaneous Motion Generation for Robots and Machines.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Sep 27 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.9.2-1
- update to latest release
* Thu Mar 09 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.9.2-1
- Initial humble build
