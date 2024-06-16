# Meta Package
Name:           ros-jazzy-tf2-eigen
Version:        0.36.4
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-tf2_eigen and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-tf2_eigen
Requires:       ros2-jazzy-tf2_eigen-devel

Obsoletes: ros-jazzy-tf2-eigen < 0.36.4-1

%description
tf2_eigen

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Jun 05 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.36.4-1
- Update to latest release
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.36.3-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.36.2-1
- Update to latest release
