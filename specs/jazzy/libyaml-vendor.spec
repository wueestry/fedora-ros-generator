# Meta Package
Name:           ros-jazzy-libyaml-vendor
Version:        1.6.3
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://github.com/yaml/libyaml
Summary:        Meta package for ros2-jazzy-libyaml_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-libyaml_vendor
Requires:       ros2-jazzy-libyaml_vendor-devel

Obsoletes: ros-jazzy-libyaml-vendor < 1.6.3-1

%description
Vendored version of libyaml.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.6.3-1
- Update to latest release
