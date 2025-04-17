# Meta Package
Name:           ros-jazzy-std-srvs
Version:        5.3.6
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-std_srvs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-std_srvs
Requires:       ros2-jazzy-std_srvs-devel

Obsoletes: ros-jazzy-std-srvs < 5.3.6-1

%description
A package containing some standard service definitions.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 05 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.5.3.6-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.5.3.5-1
- Update to latest release
